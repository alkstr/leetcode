# 2373. Largest Local Values in a Matrix
#
# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# - maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
# Return the generated matrix.

from itertools import chain
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)

        result = [[0 for _ in range(N - 2)] for _ in range(N - 2)]
        for i in range(N - 2):
            for j in range(N - 2):
                result[i][j] = max(
                    chain.from_iterable(
                        [
                            grid[i][j:j+3],
                            grid[i+1][j:j+3],
                            grid[i+2][j:j+3]
                        ]
                    )
                )

        return result


assert Solution().largestLocal(
    [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
) == [
    [9, 9],
    [8, 6]
]

assert Solution().largestLocal(
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
) == [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]
