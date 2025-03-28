# 2503. Maximum Number of Points From Grid Queries
#
# You are given an m x n integer matrix grid and an array queries of size k.
# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
# - If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# - Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
# Return the resulting array answer.

import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])
        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))

        hq = [(grid[0][0], 0, 0)]
        visited = [[False for _ in row] for row in grid]
        visited[0][0] = True

        sorted_queries = sorted(enumerate(queries), key=lambda t: t[1])
        result = [None for _ in sorted_queries]

        def _in_bounds(x, y: int) -> bool:
            return 0 <= x < M and 0 <= y < N

        count = 0
        sq_i = 0
        q_i, q_val = sorted_queries[sq_i]
        while hq:
            val, x, y = heapq.heappop(hq)

            while val >= q_val:
                result[q_i] = count
                sq_i += 1
                if sq_i == len(queries):
                    break
                q_i, q_val = sorted_queries[sq_i]

            if sq_i == len(queries):
                break

            count += 1

            for i, j in DIRECTIONS:
                if not _in_bounds(x + i, y + j) or visited[x+i][y+j]:
                    continue

                visited[x+i][y+j] = True
                adj_val = grid[x+i][y+j]
                heapq.heappush(hq, (adj_val, x+i, y+j))

        for i in range(sq_i, len(queries)):
            q_i, _ = sorted_queries[i]
            result[q_i] = count

        return result


assert Solution().maxPoints(
    [[1, 2, 3], [2, 5, 7], [3, 5, 1]],
    [5, 6, 2]
) == [5, 8, 1]

assert Solution().maxPoints(
    [[5, 2, 1], [1, 1, 2]],
    [3]
) == [0]
