# 2658. Maximum Number of Fish in a Grid
#
# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
# - A land cell if grid[r][c] = 0, or
# - A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:
# - Catch all the fish at cell (r, c), or
# - Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in row] for row in grid]
        result = 0

        def is_in_bounds(x: int, y: int):
            return x >= 0 and x < n and y >= 0 and y < m

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 0 or visited[i][j]:
                    continue

                count = 0
                deq = deque([(i, j)])
                visited[i][j] = True

                while deq:
                    x, y = deq.pop()
                    count += grid[x][y]

                    for (a, b) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if not is_in_bounds(a, b) or visited[a][b] or grid[a][b] == 0:
                            continue
                        deq.append((a, b))
                        visited[a][b] = True

                result = max(result, count)

        return result


assert Solution().findMaxFish(
    [
        [0, 2, 1, 0],
        [4, 0, 0, 3],
        [1, 0, 0, 4],
        [0, 3, 2, 0]
    ]
) == 7

assert Solution().findMaxFish(
    [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]
) == 1
