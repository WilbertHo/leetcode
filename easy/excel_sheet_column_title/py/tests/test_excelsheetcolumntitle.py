from nose.tools import eq_
import excelsheetcolumntitle


def test_excelsheetcolumntitle():
    s = excelsheetcolumntitle.Solution()
    eq_(s.convertToTitle(1), 'A')
    eq_(s.convertToTitle(26), 'Z')
    eq_(s.convertToTitle(27), 'AA')
    eq_(s.convertToTitle(28), 'AB')
