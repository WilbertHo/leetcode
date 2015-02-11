import re
import sys


class Solution(object):
    # @return a string
    def countAndSay(self, n):
        num = '1'

        for i in range(1, n):
            say = ''
            while num:
                digit = num[0]
                digit_count = len(re.search(r'^{d}+'.format(d=digit), num).group(0))
                say = say + str(digit_count) + digit
                num = num[digit_count:]
            num = say

        return num


if __name__ == '__main__':
    input = int(sys.argv[1])
    solution = Solution()
    print solution.countAndSay(input)
