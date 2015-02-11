from nose.tools import eq_

import countandsay

def test_countandsay():
    solution = countandsay.Solution()
    eq_(solution.countAndSay(1), '1')
    eq_(solution.countAndSay(2), '11')
    eq_(solution.countAndSay(3), '21')
    eq_(solution.countAndSay(4), '1211')
    eq_(solution.countAndSay(5), '111221')
