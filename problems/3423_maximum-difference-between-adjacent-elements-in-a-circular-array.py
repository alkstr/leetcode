# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
#
# Given a circular array nums, find the maximum absolute difference between adjacent elements.
# Note: In a circular array, the first and last elements are adjacent.

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = abs(nums[0] - nums[-1])
        for num_1, num_2 in zip(nums, nums[1:]):
            result = max(result, abs(num_1 - num_2))

        return result


assert Solution().maxAdjacentDistance([1, 2, 4]) == 3
assert Solution().maxAdjacentDistance([-5, -10, -5]) == 5
