from nose.tools import eq_
from validparentheses import Solution


def test_validparentheses():
    s = Solution()
    eq_(s.isValid('({[]})'), True)
    eq_(s.isValid('()[]{}'), True)
    eq_(s.isValid('([)]'), False)
    eq_(s.isValid('([{}]'), False)
    eq_(s.isValid('(()[]{})'), True)
