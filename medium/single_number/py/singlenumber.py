""" 
Given an array of integers, every element appears twice except for one.
Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?
"""
from collections import defaultdict, Counter

class Solution(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        count = defaultdict(int)
        for c in A:
            count[c] += 1
        # count = Counter(A)

        return min(count, key=count.get)


def main():
    pass


if __name__ == '__main__':
    main()
