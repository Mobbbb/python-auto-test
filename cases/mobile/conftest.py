import pytest
import time


@pytest.fixture(scope='class', autouse="true")
def setUpClassBrowser(request, selenium_driver):
    selenium_driver.get('http://www.baidu.com')
    time.sleep(2)
