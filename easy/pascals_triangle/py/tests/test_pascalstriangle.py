from nose.tools import eq_
import pascalstriangle


def test_generate():
    s = pascalstriangle.Solution()
    eq_(s.generate(0), [])
    eq_(s.generate(1), [[1]])
    eq_(s.generate(5), [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]])
    eq_(s.generate(6), [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1]])
