# 3191. Minimum Operations to Make Binary Array Elements Equal to One I
# You are given a Binary Array nums.
# You can do the following operation on the array any number of times (possibly zero):
# - Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def _flip(i: int):
            nums[i] = 0 if nums[i] == 1 else 1

        flips = 0
        for i in range(n - 2):
            if nums[i] == 1:
                continue

            _flip(i)
            _flip(i + 1)
            _flip(i + 2)
            flips += 1

        if 0 in nums:
            return -1

        return flips


assert Solution().minOperations([0, 1, 1, 1, 0, 0]) == 3
assert Solution().minOperations([0, 1, 1, 1]) == -1
