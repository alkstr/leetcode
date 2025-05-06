# 3190. Find Minimum Operations to Make All Elements Divisible by Three
#
# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
# Return the minimum number of operations to make all elements of nums divisible by 3.

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(num % 3, 3 - num % 3) for num in nums)


assert Solution().minimumOperations([1, 2, 3, 4]) == 3
assert Solution().minimumOperations([3, 6, 9]) == 0
