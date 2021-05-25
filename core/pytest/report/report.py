import os
from shutil import copyfile


def revise_pytest_report(report_path, custom_css, report_href):
    """
    修改pytest report, 改为默认收起格式
    :param report_href:
    :param custom_css:
    :param report_path:
    :return:
    """
    if report_path:
        with open(report_path + '.tmp', 'w') as fout:
            with open(report_path, 'r', encoding='utf-8') as fin:
                origin_report_lines = fin.readlines()
                origin_report_lines_len = len(origin_report_lines)
                for i in range(origin_report_lines_len):
                    # 写入css
                    if '</head>' in origin_report_lines[i]:
                        with open(custom_css, 'r') as fcss:
                            fout.write("<style>" + "\n")
                            fcss_lines = fcss.readlines()
                            fout.writelines(fcss_lines)
                            fout.write("</style>" + "\n")
                        fout.write(origin_report_lines[i].rstrip() + "\n")
                    elif i + 1 < origin_report_lines_len \
                            and '<td class="extra" colspan="4">' in origin_report_lines[i + 1]\
                            and '<tr>' in origin_report_lines[i]:
                        fout.write('<tr class="collapsed">' + "\n")
                    elif '<h2>Environment</h2>' in origin_report_lines[i]:
                        fout.write('<p>点击<a href="{url}">查看详情</a></p>'.format(url=report_href))
                        fout.write(origin_report_lines[i].rstrip() + "\n")
                    elif '<div class="log">' in origin_report_lines[i]:
                        continue
                    else:
                        fout.write(origin_report_lines[i].rstrip() + "\n")
    return report_path + '.tmp'


def copy_file(src, dst):
    if os.path.exists(src) and os.path.exists(dst):
        copyfile(src, dst)


def take_screenshot(item, driver, summary, extra):
    """
    截图并写入报告中
    :param item:
    :param driver:
    :param summary:
    :param extra:
    :return:
    """
    try:
        screenshot = driver.get_screenshot_as_base64()
    except Exception as e:
        summary.append('WARNING: Failed to gather screenshot: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add screenshot to the html report
        extra.append(pytest_html.extras.image(screenshot))


def take_page_source(item, driver, summary, extra):
    try:
        html = driver.page_source
    except Exception as e:
        summary.append('WARNING: Failed to gather Page Source: {0}'.format(e))
        return
    pytest_html = item.config.pluginmanager.getplugin('html')
    if pytest_html is not None:
        # add page source to the html report
        extra.append(pytest_html.extras.text(html, 'HTML'))
