from selenium import webdriver as BrowserWebDriver
from selenium.webdriver.chrome import webdriver as ChromeWebDriver


def init_driver(port=0, headless='0', mobile='True', user_agent='', driver_path=''):
    """
    初始化webdriver
    :param port:
    :param headless:
    :param mobile:
    :param user_agent:
    :param driver_path:
    :return:
    """
    chrome_options = BrowserWebDriver.ChromeOptions()
    if headless == '0':
        chrome_options.add_argument("--headless")
    chrome_options.add_argument('user-agent="' + user_agent + '"')
    if mobile == 'True':
        mobile_emulation = {"deviceName": "Nexus 5"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = ChromeWebDriver.WebDriver(executable_path=driver_path, port=port,
                                       desired_capabilities=chrome_options.to_capabilities())
    return driver
