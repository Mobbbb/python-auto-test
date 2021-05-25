import pytest
from py._xmlgen import html

from core.pytest.report.report import take_screenshot, take_page_source
from core.selenium import init_driver


@pytest.fixture(scope='class', autouse="true")
def setUpClassCases(request, task_id):
    """
    前置
    :param request:
    :param task_id
    :return:
    """
    request.cls.task_id = task_id


@pytest.fixture(scope='class', autouse="true")
def selenium_driver(request, selenium_driver_executable, mobile, headless):
    driver = init_driver(headless=headless, mobile=mobile, driver_path=selenium_driver_executable)
    # add to tearDown
    request.addfinalizer(driver.quit)
    return driver


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    # 增加用例描述
    description = ''
    if item.function.__doc__ is not None:
        description += ('::' + str(item.function.__doc__))
    report.description = description

    failure = report.failed

    summary = []
    extra = getattr(report, 'extra', [])
    # 获取用例中的selenium_driver
    if not hasattr(item, 'funcargs') or not 'selenium_driver' in item.funcargs:
        return
    driver = item.funcargs['selenium_driver']
    if failure:
        take_screenshot(item, driver, summary, extra)
        take_page_source(item, driver, summary, extra)
    else:
        take_screenshot(item, driver, summary, extra)

    # 增加对比截图
    if hasattr(item.cls, 'screenshots') and 'jgy' in item.cls.screenshots:
        for screenshot in item.cls.screenshots['jgy']:
            extra.append(pytest_html.extras.image(screenshot[0]))
            extra.append(pytest_html.extras.image(screenshot[1]))

    if summary:
        report.sections.append(('pytest', '\n'.join(summary)))
    report.extra = extra
