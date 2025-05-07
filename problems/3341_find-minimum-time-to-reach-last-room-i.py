# 3341. Find Minimum Time to Reach Last Room I
#
# There is a dungeon with n x m rooms arranged as a grid.
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.
# Return the minimum time to reach the room (n - 1, m - 1).
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])

        def _is_in_bounds(x: int, y: int) -> bool:
            return 0 <= x < M and 0 <= y < N

        visited = [[False for _ in moveTime[0]] for _ in moveTime]
        visited[0][0] = True
        hq = [(0, 0, 0)]
        while hq:
            time, x, y = heapq.heappop(hq)
            if (x, y) == (M - 1, N - 1):
                return time

            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if not _is_in_bounds(x + i, y + j) or visited[y+j][x+i]:
                    continue

                visited[y+j][x+i] = True
                heapq.heappush(
                    hq,
                    (max(moveTime[y+j][x+i] + 1, time + 1), x + i, y + j)
                )

        raise Exception("Unreachable")


assert Solution().minTimeToReach([[0, 4], [4, 4]]) == 6
assert Solution().minTimeToReach([[0, 0, 0], [0, 0, 0]]) == 3
assert Solution().minTimeToReach([[0, 1], [1, 2]]) == 3
