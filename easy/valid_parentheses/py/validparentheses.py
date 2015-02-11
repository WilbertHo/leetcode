import fileinput

class Solution(object):
    # @return a boolean
    def isValid(self, s):
        parentheses = {'(': ')',
                       '{': '}',
                       '[': ']'}
        stack = list()

        for c in s:
            if c in parentheses.keys():
                stack.append(c)
            if c in parentheses.values():
                # if stack is empty
                if not stack:
                    return False
                # if top of stack is c's counterpart, pop and discard both
                #   ex: (), [], {}
                elif c == parentheses[stack[-1]]:
                    stack.pop()
                # else: return False, since the stack only has [({[]
                else:
                    return False
        # If there are parens left on the stack, it's unbalanced
        return True if not stack else False


if __name__ == '__main__':
    input = [line.strip() for line in fileinput.input()].pop()
    solution = Solution()
    print solution.isValid(input)
