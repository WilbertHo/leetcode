from nose.tools import eq_
import rotatearray

def test_rotatearray():
    s = rotatearray.Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    eq_(nums, [5,6,7,1,2,3,4])
    nums = [1,2,3]
    s.rotate(nums, 1)
    eq_(nums, [3,1,2])
