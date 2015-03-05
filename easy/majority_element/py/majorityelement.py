class Solution(object):
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        from collections import Counter
        c = dict(Counter(num))
        return max(c, key=c.get)
