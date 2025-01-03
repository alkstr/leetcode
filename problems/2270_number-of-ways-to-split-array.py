# 2270. Number of Ways to Split Array
#
# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
# - The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# - There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum, right_sum = sum(nums), 0
        count = 0

        for i in range(n - 1, 0, -1):
            left_sum -= nums[i]
            right_sum += nums[i]

            if left_sum >= right_sum:
                count += 1

        return count


assert Solution().waysToSplitArray([10, 4, -8, 7]) == 2
assert Solution().waysToSplitArray([2, 3, 1, 0]) == 2
