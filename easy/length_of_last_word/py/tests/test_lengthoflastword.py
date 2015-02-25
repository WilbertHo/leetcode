from nose.tools import eq_
import lengthoflastword


def test_lengthoflastword():
    sol = lengthoflastword.Solution()
    eq_(sol.lengthOfLastWord('hello world'), 5)
    eq_(sol.lengthOfLastWord('hello world a123'), 5)
    eq_(sol.lengthOfLastWord('a '), 1)
