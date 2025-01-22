# 1765. Map of Highest Peak
#
# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
# - If isWater[i][j] == 0, cell(i, j) is a land cell.
# - If isWater[i][j] == 1, cell(i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:
# - The height of each cell must be non-negative.
# - If the cell is a water cell, its height must be 0.
# - Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter(i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.
# Return an integer matrix height of size m x n where height[i][j] is cell(i, j)'s height. If there are multiple solutions, return any of them.

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        deq = deque()
        result = [[-1 for _ in isWater[0]] for _ in isWater]

        for i, col in enumerate(isWater):
            for j, water in enumerate(col):
                if water:
                    deq.append((i, j))
                    result[i][j] = 0

        level = 0
        while deq:
            level_count = len(deq)
            for _ in range(level_count):
                i, j = deq.pop()

                if i > 0 and result[i-1][j] == -1:
                    deq.appendleft((i - 1, j))
                    result[i-1][j] = level + 1
                if i < n - 1 and result[i+1][j] == -1:
                    deq.appendleft((i + 1, j))
                    result[i+1][j] = level + 1
                if j > 0 and result[i][j-1] == -1:
                    deq.appendleft((i, j - 1))
                    result[i][j-1] = level + 1
                if j < m - 1 and result[i][j+1] == -1:
                    deq.appendleft((i, j + 1))
                    result[i][j+1] = level + 1
            level += 1

        return result


assert Solution().highestPeak([[0, 1], [0, 0]]) == [[1, 0], [2, 1]]

assert Solution().highestPeak(
    [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
