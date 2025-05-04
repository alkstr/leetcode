# 1128. Number of Equivalent Domino Pairs
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        counter = [[0 for _ in range(10)] for _ in range(10)]

        for i, j in dominoes:
            if i > j:
                i, j = j, i

            count += counter[i][j]
            counter[i][j] += 1

        return count


assert Solution().numEquivDominoPairs(
    [[1, 2], [2, 1], [3, 4], [5, 6]]
) == 1

assert Solution().numEquivDominoPairs(
    [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
) == 3
