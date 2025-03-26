# 2033. Minimum Operations to Make a Uni-Value Grid
#
# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
# A uni-value grid is a grid where all the elements of it are equal.
# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

from itertools import chain
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = chain.from_iterable(grid)
        common_remainder = grid[0][0] % x
        for num in nums:
            if num % x != common_remainder:
                return -1

        nums = sorted(chain.from_iterable(grid))
        median = nums[len(nums) // 2]
        count = sum(abs(num - median) // x for num in nums)

        return count


assert Solution().minOperations(
    [[529, 529, 989], [989, 529, 345], [989, 805, 69]],
    92
) == 25

assert Solution().minOperations([[2, 4], [6, 8]], 2) == 4
assert Solution().minOperations([[1, 5], [2, 3]], 1) == 5
assert Solution().minOperations([[1, 2], [3, 4]], 2) == -1
