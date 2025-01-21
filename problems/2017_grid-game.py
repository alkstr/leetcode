# 2017. Grid Game
#
# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.
# Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
# At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.
# The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        total_top_points, total_bot_points = sum(grid[0]), sum(grid[1])
        top_points, bot_points = grid[0][0], total_bot_points
        second_score = (total_top_points - grid[0][0], 0)

        for i in range(1, m):
            top_points += grid[0][i]
            bot_points -= grid[1][i-1]
            new_second_score = (
                total_top_points - top_points,
                total_bot_points - bot_points
            )
            if max(second_score) > max(new_second_score):
                second_score = new_second_score

        return max(second_score)


assert Solution().gridGame([[2, 5, 4], [1, 5, 1]]) == 4
assert Solution().gridGame([[3, 3, 1], [8, 5, 2]]) == 4
assert Solution().gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]) == 7
