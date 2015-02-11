from nose.tools import eq_
import excelcolumncountnumber

def test_excelcolumncountnumber():
    solution = excelcolumncountnumber.Solution()
    eq_(solution.titleToNumber('A'), 1)
    eq_(solution.titleToNumber('B'), 2)
    eq_(solution.titleToNumber('Z'), 26)
    eq_(solution.titleToNumber('AA'), 27)
    eq_(solution.titleToNumber('AB'), 28)
    eq_(solution.titleToNumber('BA'), 53)
