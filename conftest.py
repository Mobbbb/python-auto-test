import pytest


def pytest_addoption(parser):
    parser.addoption("--port", help="appium server port", default=4723)
    parser.addoption("--task_id", help="report relative path", default="")
    parser.addoption("--selenium_driver_executable", help="selenium_driver_executable path", default="")
    parser.addoption("--headless", help="if headless browser", default="")
    parser.addoption("--baseline_url", help="baseline_url", default="")
    parser.addoption("--testing_url", help="testing url", default="")
    parser.addoption("--mock", help="mock", default="")
    parser.addoption("--mobile", help="mobile", default="")


@pytest.fixture(scope='session')
def port(request):
    """
    appium服务器端口
    :param request:
    :return:
    """
    return request.config.getoption('port')


@pytest.fixture(scope='session')
def task_id(request):
    return request.config.getoption('task_id')


@pytest.fixture(scope='session')
def headless(request):
    return request.config.getoption('headless')


@pytest.fixture(scope='session')
def baseline_url(request):
    return request.config.getoption('baseline_url')


@pytest.fixture(scope='session')
def testing_url(request):
    return request.config.getoption('testing_url')


@pytest.fixture(scope='session')
def mock(request):
    return request.config.getoption('mock')


@pytest.fixture(scope='session')
def selenium_driver_executable(request):
    return request.config.getoption('selenium_driver_executable')


@pytest.fixture(scope='session')
def mobile(request):
    return request.config.getoption('mobile')
