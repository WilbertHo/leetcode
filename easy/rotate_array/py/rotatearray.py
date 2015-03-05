"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""

class Solution(object):
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        steps = -1 * k % len(nums)
        for i, elem in enumerate(nums[steps:] + nums[:steps]):
            nums[i] = elem


def main():
    s = Solution()
    num = [1,2,3,4,5,6,7]
    s.rotate(num, 3)
    print num


if __name__ == '__main__':
    main()
