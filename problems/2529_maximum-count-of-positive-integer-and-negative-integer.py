# 2529. Maximum Count of Positive Integer and Negative Integer
#
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
# - In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

from typing import List, Optional


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        if nums[0] > 0:
            return n
        if nums[-1] < 0:
            return n
        if nums[0] == 0 and nums[-1] == 0:
            return 0

        def binary_search_neg() -> Optional[int]:
            left, right = 0, n - 1
            while left <= right:
                i = (left + right) // 2
                if nums[i] < 0 and nums[i+1] >= 0:
                    return i

                if nums[i] < 0:
                    left = i + 1
                elif nums[i] >= 0:
                    right = i - 1

            return None

        def binary_search_pos() -> Optional[int]:
            left, right = 0, n - 1
            while left <= right:
                i = (left + right) // 2
                if nums[i] > 0 and nums[i-1] <= 0:
                    return i

                if nums[i] <= 0:
                    left = i + 1
                elif nums[i] > 0:
                    right = i - 1

            return None

        last_neg = binary_search_neg()
        first_pos = binary_search_pos()

        neg_count = 0 if last_neg is None else last_neg + 1
        pos_count = 0 if first_pos is None else n - first_pos

        return max(neg_count, pos_count)


assert Solution().maximumCount([-2, -1, -1, 1, 2, 3]) == 3
assert Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2]) == 3
assert Solution().maximumCount([5, 20, 66, 1314]) == 4
