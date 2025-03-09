# 3208. Alternating Groups II
#
# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
# - colors[i] == 0 means that tile i is red.
# - colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
# Return the number of alternating groups.
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors_counter = 1
        groups = 0

        for i in range(-k + 2, n):
            if colors[i] != colors[i-1]:
                colors_counter += 1
            else:
                colors_counter = 1
                continue

            if colors_counter >= k:
                groups += 1

        return groups


assert Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3) == 3
assert Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6) == 2
assert Solution().numberOfAlternatingGroups([1, 1, 0, 1], 4) == 0
