#!/usr/bin/env pytho
"""
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.

    For example, 
    Given s = "Hello World",
    return 5.
"""

import fileinput
import re


class Solution(object):
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        """ Return the length of the last word """
        for word in reversed(re.split(r'\s+', s)):
            if not word:
                continue
            if re.search(r'[^a-zA-Z]', word):
                continue
            return len(word)

        return 0


def main():
    input = [line.strip() for line in fileinput.input()]
    sol = Solution()
    print sol.lengthOfLastWord(input.pop())


if __name__ == '__main__':
    main()
