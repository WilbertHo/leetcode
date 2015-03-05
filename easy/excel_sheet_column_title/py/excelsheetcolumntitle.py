""" 
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""

class Solution(object):
    # @return a string
    def convertToTitle(self, num):
        from string import uppercase

        alphabet_length = len(uppercase)
        alphabet = dict(zip(range(1, alphabet_length + 1), uppercase))

        title = ''

        """
            The issue is, with 1 -> A, we have no zero meaning
            26 -> Z will be a problem. So, we have to deal with going
            from 25 -> 'Y' to 26 -> 'A0'

            We'll do this by returning 'Z' when we request a 0 from
            the alphabet dictionary since 26 % 25 == 0. If we
            have a 0 we'll subtract 1 from the division that
            follows.

            Ex:
            convertToTitle(26)
            26 / 26 == 1, R0, title == 'Z' + ''
            1 / 26 == 0, R1, title == 'A' + 'Z' *Problem*

            So, to correct this, when num % 26 == 0, we'll
            subtract 1 from num / alphabet_length
            26 / 26 == 1, R0, title == 'Z' + ''
            num = (26 / 26) - 1 since R == 0

            Another example:
            convertToTitle(52)
            52 / 26 == 2, R0, title == 'Z' + ''
            num (52 / 26) - 1 since R == 0
            1 / 26 == 0, R1, title = 'A' + 'Z' + ''
        """
        while num > 0:
            remainder = num % alphabet_length
            title = alphabet.get(remainder, 'Z') + title
            num = num / alphabet_length - (1 if remainder == 0 else 0)

        return title
