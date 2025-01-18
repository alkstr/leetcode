# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
#
# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
# - 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# - 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# - 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# - 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.
# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
# Return the minimum cost to make the grid have at least one valid path.

from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n_1, n_2 = len(grid), len(grid[0])
        min_cost = [[10_000 for _ in range(n_2)] for _ in range(n_1)]
        min_cost[0][0] = 0
        deq = deque([(0, 0)])

        while deq:
            i, j = deq.pop()

            if j < n_2 - 1:
                if grid[i][j] == 1 and min_cost[i][j] < min_cost[i][j+1]:
                    deq.append((i, j + 1))
                    min_cost[i][j+1] = min_cost[i][j]
                elif min_cost[i][j] + 1 < min_cost[i][j+1]:
                    deq.appendleft((i, j + 1))
                    min_cost[i][j+1] = min_cost[i][j] + 1

            if j > 0:
                if grid[i][j] == 2 and min_cost[i][j] < min_cost[i][j-1]:
                    deq.append((i, j - 1))
                    min_cost[i][j-1] = min_cost[i][j]
                elif min_cost[i][j] + 1 < min_cost[i][j-1]:
                    deq.appendleft((i, j - 1))
                    min_cost[i][j-1] = min_cost[i][j] + 1

            if i < n_1 - 1:
                if grid[i][j] == 3 and min_cost[i][j] < min_cost[i+1][j]:
                    deq.append((i + 1, j))
                    min_cost[i+1][j] = min_cost[i][j]
                elif min_cost[i][j] + 1 < min_cost[i+1][j]:
                    deq.appendleft((i + 1, j))
                    min_cost[i+1][j] = min_cost[i][j] + 1

            if i > 0:
                if grid[i][j] == 4 and min_cost[i][j] < min_cost[i-1][j]:
                    deq.append((i - 1, j))
                    min_cost[i-1][j] = min_cost[i][j]
                elif min_cost[i][j] + 1 < min_cost[i-1][j]:
                    deq.appendleft((i - 1, j))
                    min_cost[i-1][j] = min_cost[i][j] + 1

        return min_cost[-1][-1]


assert Solution().minCost(
    [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
) == 3

assert Solution().minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]) == 0
assert Solution().minCost([[1, 2], [4, 3]]) == 1
