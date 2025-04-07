# 416. Partition Equal Subset Sum
#
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        TOTAL = sum(nums)
        if TOTAL % 2:
            return False
        HALF = TOTAL // 2

        dp = [False for _ in range(HALF + 1)]
        dp[0] = True

        for num in nums:
            for i in range(HALF, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[HALF]


assert Solution().canPartition([3, 3, 3, 4, 5])

assert Solution().canPartition([1, 5, 11, 5])
assert not Solution().canPartition([1, 2, 3, 5])
