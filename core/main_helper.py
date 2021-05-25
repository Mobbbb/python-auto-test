import argparse
import os
from datetime import datetime

from core.pytest.command import execute_command
from core.pytest.report.report import copy_file, revise_pytest_report
from core.pytest.run.test_loader import load_cases, get_root_dir

from settings import REPORT_DIR, PYTEST_PATH, REPORT_URL_PREFIX, ROOT_DIR, WEB_DRIVER_PATH


def build_params():
    """
    解析command line 参数
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--headless", choices=['0', '1'],
                        help="0: 无头浏览器模式, 1: 正常模式", default='0')
    parser.add_argument("-t", "--type", choices=['mobile'],  # TODO
                        help="mobile: 模拟手机浏览器测试cases\mobile中的用例", default='')
    parser.add_argument("--title", default="测试报告")
    parser.add_argument("--script", help="指定运行的脚本")
    parser.add_argument("--testing_url", help="测试链接地址", default='')
    parser.add_argument("--baseline_url", help="对比链接地址, 默认不对比", default='')
    parser.add_argument("--parallel", help="用例并行运行个数(会启动n个浏览器), 1为默认", default=1)
    parser.add_argument("--reruns", help="用例失败后重跑次数, 默认不重跑", default=0)
    parser.add_argument("--mock", help="是否使用mock接口, 默认不使用", default=0)
    args = parser.parse_args()

    print('args', vars(args))
    return args


def stop_server(service):
    if service:
        service.stop()


def run_browser(title, case_pattern, reruns, parallel, headless, mock, testing_url, baseline_url):
    """
    运行browser用例
    :return:
    """
    cases = load_cases('mobile', case_pattern)
    print('cases to run', cases)
    task_id = 'browser_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    report_path = os.path.join(REPORT_DIR, task_id, "report", title + ".html")
    # build command
    cmd_str = build_browser_param_str(report_path, task_id, get_root_dir('mobile'), cases, reruns, parallel, headless,
                                      mock,
                                      True,
                                      WEB_DRIVER_PATH,
                                      testing_url, baseline_url)

    run_base(task_id, title, cases, cmd_str)


def run_base(task_id, title, cases, cmd_str):
    report_path = os.path.join(REPORT_DIR, task_id, "report", title + ".html")
    report_assets_path = os.path.join(REPORT_DIR, task_id, "report", "assets")
    report_css_path = os.path.join(report_assets_path, 'style.css')
    report_href = os.path.join(REPORT_URL_PREFIX, task_id, "report", title + ".html")
    if not os.path.exists(report_assets_path):
        os.makedirs(report_assets_path)

    if cases and len(cases) > 0:
        print('cmd_str', cmd_str)
        output = execute_command(cmd_str)
        print(output)

        report_assets_path = os.path.join(ROOT_DIR, 'core', 'pytest', 'report', 'assets')
        # 替换pytest默认css
        copy_file(os.path.join(report_assets_path, 'pytest_custom.css'), report_css_path)

        """
        1. 将css样式改为embedded
        2. 默认collapsed
        3. 插入访问超链接 
        以支持邮件格式
        """
        revised_report = revise_pytest_report(report_path, os.path.join(report_assets_path, 'pytest_custom_email.css'), report_href)


def build_browser_param_str(report_path, task_id, root_dir, python_files, rerun_count, xdistn,
                            headless,
                            mock,
                            mobile,
                            selenium_driver_executable,
                            testing_url, baseline_url=""):
    cmd_to_run = PYTEST_PATH + ' {report_path_option} ' \
                               '{task_id_option} ' \
                               '{selenium_driver} ' \
                               '{root_dir_option} ' \
                               '{rerun_option} ' \
                               '{xdist_option} ' \
                               '{headless_option} ' \
                               '{mobile_option} ' \
                               '{mock_option} ' \
                               '{baseline_url_option} ' \
                               '{testing_url_option} ' \
                               '{all_cases_options}'.format(
                                    report_path_option='--html="{report_path}"'.format(report_path=report_path),
                                    task_id_option='--task_id={task_id}'.format(task_id=task_id),
                                    selenium_driver='--selenium_driver_executable={selenium_driver_executable}'.format(selenium_driver_executable=selenium_driver_executable),
                                    root_dir_option='--rootdir="{root_dir}"'.format(root_dir=root_dir),
                                    all_cases_options=(' '.join(python_files)),
                                    rerun_option='--reruns={rerun_count} --count=1'.format(rerun_count=rerun_count),
                                    xdist_option='-n {xdistn} --dist=loadfile'.format(xdistn=xdistn),
                                    headless_option='--headless={headless}'.format(headless=headless),
                                    mobile_option='--mobile={mobile}'.format(mobile=mobile),
                                    mock_option='--mock={mock}'.format(mock=mock),
                                    baseline_url_option='--baseline_url={baseline_url}'.format(baseline_url=baseline_url),
                                    testing_url_option='--testing_url={testing_url}'.format(testing_url=testing_url),
                                )
    print('cmd_to_run', cmd_to_run)
    return cmd_to_run
