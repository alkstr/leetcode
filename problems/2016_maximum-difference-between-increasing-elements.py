# 2016. Maximum Difference Between Increasing Elements
#
# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        min_prefix = [0 for _ in nums]
        min_prefix[0] = nums[0]
        for i in range(1, n):
            min_prefix[i] = min(min_prefix[i-1], nums[i])

        max_postfix = [0 for _ in nums]
        max_postfix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            max_postfix[i] = max(max_postfix[i+1], nums[i])

        result = max(
            max_n - min_n
            for min_n,
            max_n in zip(min_prefix, max_postfix)
        )
        result = -1 if result <= 0 else result
        return result


assert Solution().maximumDifference([7, 1, 5, 4]) == 4
assert Solution().maximumDifference([9, 4, 3, 2]) == -1
assert Solution().maximumDifference([1, 5, 2, 10]) == 9
