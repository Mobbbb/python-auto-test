import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# pytest运行路径
PYTEST_PATH = '"D:\\Anaconda3\\Scripts\\pytest.exe"'

# 用例根路径, 默认为项目中的cases目录
CASES_ROOT = os.path.join(ROOT_DIR, 'cases')

# 测试结果存储路径
REPORT_DIR = 'F:\\project\\auto-test-util\\Report'

# 测试结果图片存储路径
REPORT_IMG_DIR = os.path.join(REPORT_DIR, 'img')

# chromedriver路径
WEB_DRIVER_PATH = '"F:\\project\\auto-test-util\\chromedriver.exe"'

# 测试结果前缀路径
REPORT_URL_PREFIX = ''

