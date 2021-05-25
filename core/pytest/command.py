import shlex
import subprocess


def execute_command(command):
    """
    执行命令
    :param command:
    :return:
    """
    result = subprocess.run(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, timeout=None, universal_newlines=True)
    return result.stdout
