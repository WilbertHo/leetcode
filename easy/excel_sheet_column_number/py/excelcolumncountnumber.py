import string

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        alphabet = dict(zip(string.ascii_uppercase,
                            range(1, 27)))
        column = 0
        for power, digit in enumerate(s[::-1]):
            column += alphabet.get(digit) * 26**power

        return column
