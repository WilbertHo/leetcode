"""
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example, [1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

class Solution(object):
    """ Permutations of [1,2,3,4] can be reduced to finding
        permutations of 1 + [2,3,4], 2 + [1,3,4], 3 + [1,2,4]
        and 4 + [1,2,3]
        [2,3,4] can be reduced to 2 + [3,4] and so on.
        [1,2] can be reduced to 1 + [2] and 2 + [1]
    """
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        def permute_recur(n):
            """ Convert our lists to tuples since tuples are hashable
                and lists are not. This comes in handy later when we
                run set().
            """
            if len(n) == 1:
                return [tuple(n)]
            permutations = []
            for (i, elem) in enumerate(n):
                subpermutations = permute_recur(n[:i] + n[i+1:])
                total = ((elem,) + sub for sub in subpermutations)
                permutations.extend(total)
            return permutations

        permutations = permute_recur(num)
        unique_permutations = set(permutations)

        # Convert tuples back to a list for output
        return map(list, unique_permutations)


def main():
    pass


if __name__ == '__main__':
    main()
