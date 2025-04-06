# 368. Largest Divisible Subset
#
# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
# - answer[i] % answer[j] == 0, or
# - answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1 for _ in nums]
        prev = [None for _ in nums]

        for i, num in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if num % nums[j] != 0:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        max_i, max_count = 0, dp[0]
        for i, count in enumerate(dp):
            if count <= max_count:
                continue
            max_i, max_count = i, count

        result = []
        i = max_i
        while i is not None:
            result.append(nums[i])
            i = prev[i]
        result.reverse()

        return result


assert Solution().largestDivisibleSubset([1, 2, 3]) == [1, 2]
assert Solution().largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]
