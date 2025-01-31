# 827. Making A Large Island
#
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        group_to_size = dict()
        group = [[None for _ in range(n)] for _ in range(n)]
        current_group = 0

        def _is_in_bounds(x: int, y: int) -> bool:
            return x >= 0 and x < n and y >= 0 and y < n

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 0 or group[i][j]:
                    continue
                current_group += 1
                group_to_size[current_group] = 0

                deq = deque([(i, j)])
                group[i][j] = current_group
                group_to_size[current_group] += 1

                while deq:
                    x, y = deq.popleft()

                    for (a, b) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if not _is_in_bounds(a, b) or grid[a][b] == 0 or group[a][b]:
                            continue

                        deq.append((a, b))
                        group[a][b] = current_group
                        group_to_size[current_group] += 1

        result = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    continue

                current_groups = []
                for (a, b) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if _is_in_bounds(a, b) and group[a][b] and group[a][b] not in current_groups:
                        current_groups.append(group[a][b])
                result = max(
                    result,
                    sum([group_to_size[g] for g in current_groups]) + 1
                )

        return result if result != 0 else max(group_to_size.values())


assert Solution().largestIsland([[1, 0], [0, 1]]) == 3
assert Solution().largestIsland([[1, 1], [1, 0]]) == 4
assert Solution().largestIsland([[1, 1], [1, 1]]) == 4
