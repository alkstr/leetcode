# 2444. Count Subarrays With Fixed Bounds
#
# You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
# - The minimum value in the subarray is equal to minK.
# - The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
# A subarray is a contiguous part of an array.

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        last_min, last_max, last_invalid = -1, -1, -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            count += max(0, min(last_min, last_max) - last_invalid)

        return count


assert Solution().countSubarrays([1, 3, 5, 2, 7, 5], 1, 5) == 2
assert Solution().countSubarrays([1, 1, 1, 1], 1, 1) == 10
