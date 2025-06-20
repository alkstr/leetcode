# 3443. Maximum Manhattan Distance After K Changes
#
# You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:
# - 'N' : Move north by 1 unit.
# - 'S' : Move south by 1 unit.
# - 'E' : Move east by 1 unit.
# - 'W' : Move west by 1 unit.
# Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.
# Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
# The Manhattan Distance between two cells (x_i, y_i) and (x_j, y_j) is |x_i - x_j| + |y_i - y_j|.


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        result = 0
        for i, direction in enumerate(s):
            match direction:
                case "N":
                    y += 1
                case "S":
                    y -= 1
                case "W":
                    x += 1
                case "E":
                    x -= 1
            result = max(result, min(abs(y) + abs(x) + k * 2, i + 1))
        return result


assert Solution().maxDistance("NWSE", 1) == 3
assert Solution().maxDistance("NSWWEW", 3) == 6
