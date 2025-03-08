# 2379. Minimum Recolors to Get K Consecutive Black Blocks
#
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks) + 1 - k
        white = blocks[:k].count("W")
        black = k - white
        min_count = white

        for i in range(1, n):
            prev, new = blocks[i-1], blocks[i+k-1]

            match (prev, new):
                case ("W", "B"):
                    white -= 1
                    black += 1
                case ("B", "W"):
                    black -= 1
                    white += 1

            min_count = min(min_count, white)

        return min_count


assert Solution().minimumRecolors("WBBWWBBWBW", 7) == 3
assert Solution().minimumRecolors("WBWBBBW", 2) == 0
