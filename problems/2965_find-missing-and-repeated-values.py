# 2965. Find Missing and Repeated Values
#
# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n^2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2

        current_sum = sum(sum(row) for row in grid)
        current_square_sum = sum(sum(i * i for i in row) for row in grid)

        correct_sum = n * (n + 1) // 2
        correct_square_sum = correct_sum * (2 * n + 1) // 3

        just_diff = current_sum - correct_sum
        square_diff = current_square_sum - correct_square_sum

        a = (square_diff + just_diff ** 2) // (2 * just_diff)
        b = (square_diff - just_diff ** 2) // (2 * just_diff)

        return [a, b]


assert Solution().findMissingAndRepeatedValues(
    [[1, 3], [2, 2]]
) == [2, 4]

assert Solution().findMissingAndRepeatedValues(
    [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
) == [9, 5]
