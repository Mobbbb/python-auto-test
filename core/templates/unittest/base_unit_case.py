import re


class BaseUnitCase:
    """
    自定义UnitTestCase
    类似Python UnitTest提供基础方法
    """
    def assertGreaterEqual(self, a, b, msg=''):
        assert a >= b, msg + '失败'
        print(msg, '成功')

    def assertLessEqual(self, a, b, msg=''):
        assert a <= b, msg + '失败'
        print(msg, '成功')

    def assertRegex(self, string, pattern, msg=''):
        assert re.search(pattern, string, re.MULTILINE), msg + '失败'
        print(msg, '成功')

    def assertNotRegex(self, string, pattern, msg=''):
        assert not re.match(pattern, string), msg + '失败'
        print(msg, '成功')

    def assertIsNotNone(self, value, msg=''):
        assert value is not None, msg + '失败'
        print(msg, '成功')

    def assertEqual(self, a, b, msg=''):
        assert a == b, msg + '失败'
        print(msg, '成功')

    def assertNotEqual(self, a, b, msg=''):
        assert a != b, msg + '失败'
        print(msg, '成功')

    def assertTrue(self, a, msg=''):
        assert a is True, msg + '失败'
        print(msg, '成功')

    def assertFalse(self, a, msg=''):
        assert a is False, msg + '失败'
        print(msg, '成功')

    def assertIn(self, a, b, msg=''):
        assert a in b, msg + '失败'
        print(msg, '成功')

    def assertNotIn(self, a, b, msg=''):
        assert a not in b, msg + '失败'
        print(msg, '成功')
