# 1007. Minimum Domino Rotations For Equal Row
#
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
# If it cannot be done, return -1.

from typing import Counter, List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        top_counter = Counter(tops)
        bottom_counter = Counter(bottoms)

        target = None
        for score in (1, 2, 3, 4, 5, 6):
            if top_counter[score] + bottom_counter[score] >= N:
                target = score
                break

        if target is None:
            return -1

        for top_score, bottom_score in zip(tops, bottoms):
            if top_score != target and bottom_score != target:
                return -1

        count = min(N - tops.count(target), N - bottoms.count(target))
        return count


assert Solution().minDominoRotations(
    [2, 1, 2, 4, 2, 2],
    [5, 2, 6, 2, 3, 2]
) == 2

assert Solution().minDominoRotations(
    [3, 5, 1, 2, 3],
    [3, 6, 3, 3, 4]
) == -1
