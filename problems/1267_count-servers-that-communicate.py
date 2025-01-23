# 1267. Count Servers that Communicate
#
# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [0 for _ in grid]
        cols = [0 for _ in grid[0]]
        result = 0

        for i, row in enumerate(grid):
            for j, is_occupied in enumerate(row):
                if is_occupied:
                    rows[i] += 1
                    cols[j] += 1

        for i, row in enumerate(grid):
            for j, is_occupied in enumerate(row):
                if is_occupied and (rows[i] > 1 or cols[j] > 1):
                    result += 1

        return result


assert Solution().countServers([[1, 0], [0, 1]]) == 0
assert Solution().countServers([[1, 0], [1, 1]]) == 3

assert Solution().countServers(
    [
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
) == 4
