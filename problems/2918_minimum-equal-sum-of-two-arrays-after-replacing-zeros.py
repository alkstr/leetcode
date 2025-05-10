# 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
#
# You are given two arrays nums1 and nums2 consisting of positive integers.
# You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.
# Return the minimum equal sum you can obtain, or -1 if it is impossible.

from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_count_1, zero_count_2 = nums1.count(0), nums2.count(0)
        min_sum_1 = sum(nums1) + zero_count_1
        min_sum_2 = sum(nums2) + zero_count_2

        if (
            zero_count_1 == 0 and min_sum_2 > min_sum_1
            or zero_count_2 == 0 and min_sum_1 > min_sum_2
        ):
            return -1

        return max(min_sum_1, min_sum_2)


assert Solution().minSum([3, 2, 0, 1, 0], [6, 5, 0]) == 12
assert Solution().minSum([2, 0, 2, 0], [1, 4]) == -1
