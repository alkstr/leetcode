# 1931. Painting a Grid With Three Different Colors
#
# You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.
# Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 10^9 + 7.

from collections import defaultdict


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        mask_to_colors = dict()

        for mask in range(3 ** m):
            colors = list()
            current_mask = mask
            for _ in range(m):
                colors.append(current_mask % 3)
                current_mask //= 3

            if any(color_1 == color_2 for color_1, color_2 in zip(colors, colors[1:])):
                continue

            mask_to_colors[mask] = colors

        mask_to_adj = defaultdict(list)
        for mask_2, colors_1 in mask_to_colors.items():
            for mask, colors_2 in mask_to_colors.items():
                if all(color_1 != color_2 for color_1, color_2 in zip(colors_1, colors_2)):
                    mask_to_adj[mask_2].append(mask)

        mask_to_count = [
            1 if mask in mask_to_colors else 0
            for mask
            in range(3 ** m)
        ]
        for _ in range(1, n):
            dp = [0 for _ in range(3 ** m)]
            for mask in mask_to_colors:
                dp[mask] += sum(mask_to_count[m] for m in mask_to_adj[mask])
                dp[mask] %= MOD

            mask_to_count = dp

        result = sum(mask_to_count) % MOD
        return result


assert Solution().colorTheGrid(1, 1) == 3
assert Solution().colorTheGrid(1, 2) == 6
assert Solution().colorTheGrid(5, 5) == 580986
