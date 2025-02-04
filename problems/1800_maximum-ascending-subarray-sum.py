# 1800. Maximum Ascending Subarray Sum
#
# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
# A subarray is defined as a contiguous sequence of numbers in an array.
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum, max_sum = nums[0], nums[0]

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum


assert Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65
assert Solution().maxAscendingSum([10, 20, 30, 40, 50]) == 150
assert Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33
