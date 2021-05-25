import os
import platform

from core.util.base_util import execute_command


CHROMEDRIVER_CHROME_MAPPING = {
  # Chromedriver version: minumum Chrome version
  '76.0.3809.68': '76.0.3809.68',
  '76.0.3809.25': '76.0.3809.25',
  '76.0.3809.12': '76.0.3809.12',
  '75.0.3770.140': '75.0.3770.140',
  '75.0.3770.90': '75.0.3770.90',
  '75.0.3770.8': '75.0.3770.8',
  '74.0.3729.6': '74.0.3729',
  '73.0.3683.68': '70.0.3538',
  '2.46': '71.0.3578',
  '2.45': '70.0.0',
  '2.44': '69.0.3497',
  '2.43': '69.0.3497',
  '2.42': '68.0.3440',
  '2.41': '67.0.3396',
  '2.40': '66.0.3359',
  '2.39': '66.0.3359',
  '2.38': '65.0.3325',
  '2.37': '64.0.3282',
  '2.36': '63.0.3239',
  '2.35': '62.0.3202',
  '2.34': '61.0.3163',
  '2.33': '60.0.3112',
  '2.32': '59.0.3071',
  '2.31': '58.0.3029',
  '2.30': '58.0.3029',
  '2.29': '57.0.2987',
  '2.28': '55.0.2883',
  '2.27': '54.0.2840',
  '2.26': '53.0.2785',
  '2.25': '53.0.2785',
  '2.24': '52.0.2743',
  '2.23': '51.0.2704',
  '2.22': '49.0.2623',
  '2.21': '46.0.2490',
  '2.20': '43.0.2357',
  '2.19': '43.0.2357',
  '2.18': '43.0.2357',
  '2.17': '42.0.2311',
  '2.16': '42.0.2311',
  '2.15': '40.0.2214',
  '2.14': '39.0.2171',
  '2.13': '38.0.2125',
  '2.12': '36.0.1985',
  '2.11': '36.0.1985',
  '2.10': '33.0.1751',
  '2.9': '31.0.1650',
  '2.8': '30.0.1573',
  '2.7': '30.0.1573',
  '2.6': '29.0.1545',
  '2.5': '29.0.1545',
  '2.4': '29.0.1545',
  '2.3': '28.0.1500',
  '2.2': '27.0.1453',
  '2.1': '27.0.1453',
  '2.0': '27.0.1453',
}


def get_android_chrome_version(device=''):
    """
    获取设备的webview版本
    :param device:
    :return:
    """
    result = execute_command('adb -s {0} shell dumpsys package com.google.android.webview | grep versionName'.format(device))
    if '=' in result:
        return result.split('=')[1]
    return ''


def get_most_recent_android_chrome_driver(device, path_prefix):
    """
    获取设备对应版本chromedriver路径
    :param device:
    :param path_prefix:
    :return:
    """
    target_chrome_driver_version = ''
    if device:
        chrome_version = get_android_chrome_version(device)
        print('current device {0}, chrome version: {1}'.format(device, chrome_version))
        device_chrome_version_subs = chrome_version.split('.')
        for driver_version, chrome_version in CHROMEDRIVER_CHROME_MAPPING.items():
            chrome_version_subs = chrome_version.split('.')
            is_less_than = False
            for index, sub in enumerate(chrome_version_subs):
                if device_chrome_version_subs[index] and device_chrome_version_subs[index] < sub:
                    is_less_than = True
                    break
            if not is_less_than:
                target_chrome_driver_version = chrome_version_subs[0]
                break

    system_name = get_system_name()
    chrome_driver_name = 'chromedriver'
    if system_name == 'windows':
        chrome_driver_name = 'chromedriver.exe'

    target_chrome_driver_path = os.path.join(path_prefix, target_chrome_driver_version, system_name, chrome_driver_name)
    if not os.path.exists(target_chrome_driver_path):
        print('无法找到chromedriver版本{0} 路径: {1}'.format(target_chrome_driver_version, target_chrome_driver_path))
    else:
        print('chromedriver版本{0} 路径: {1}'.format(target_chrome_driver_version, target_chrome_driver_path))
    return target_chrome_driver_path


def get_system_name():
    return platform.system().lower()


if __name__ == '__main__':
    get_android_chrome_version('UYT5T18409026041')
