"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from collections import deque

class Solution(object):
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        triangle = [[1]]
        for n in range(1, numRows):
            middle = deque(map(lambda (x,y): x + y,
                               zip(triangle[n-1], triangle[n-1][1:])))
            middle.appendleft(1)
            middle.append(1)
            triangle.append(list(middle))
        return triangle


def main():
    s = Solution()
    print generate(5)


if __name__ == '__main__':
    main()
