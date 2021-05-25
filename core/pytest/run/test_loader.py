import glob
import os

from settings import CASES_ROOT


def load_cases(type, case_pattern):
    """
    读取测试用例
    :param type: mobile
    :param case_pattern:
    :return:
    """
    root_dir = get_root_dir(type)

    if root_dir:
        return get_cases(root_dir, case_pattern)
    else:
        return []


def get_cases(dir, case_pattern='*'):
    """
    获取脚本的用例
    :param dir
    :param case_pattern
    :return:
    """
    if not os.path.isdir(dir):
        return []

    if not case_pattern:
        case_pattern = '*.py'
    result = []

    for path in glob.glob(dir + '/**/*' + case_pattern, recursive=True):
        if not path.endswith('.py'):
            continue
        result.append('"' + path + '"')
    return result


def get_root_dir(type):
    """
    获取测试脚本
    :param type: 运行 /cases 目录下的子目录名称
    :return:
    """
    if type == 'mobile':
        return os.path.join(CASES_ROOT, 'mobile')
