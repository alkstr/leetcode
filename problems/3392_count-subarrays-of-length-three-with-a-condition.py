# 3392. Count Subarrays of Length Three With a Condition
# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum((i + k) * 2 == j for i, j, k in zip(nums[:-2], nums[1:-1], nums[2:]))


assert Solution().countSubarrays([1, 2, 1, 4, 1]) == 1
assert Solution().countSubarrays([1, 1, 1]) == 0
