# 2873. Maximum Value of an Ordered Triplet I
#
# You are given a 0-indexed integer array nums.
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_element = max_diff = max_result = 0
        for num in nums:
            max_result = max(max_result, max_diff * num)
            max_diff = max(max_diff, max_element - num)
            max_element = max(max_element, num)

        return max_result


assert Solution().maximumTripletValue([12, 6, 1, 2, 7]) == 77
assert Solution().maximumTripletValue([1, 10, 3, 4, 19]) == 133
assert Solution().maximumTripletValue([1, 2, 3]) == 0
