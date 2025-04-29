# 2962. Count Subarrays Where Max Element Appears at Least K Times
#
# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
# A subarray is a contiguous sequence of elements within an array.

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)

        max_element = max(nums)
        max_count = 0
        total = 0
        end = -1
        for start in range(N):
            while end < N - 1 and max_count < k:
                end += 1
                max_count += nums[end] == max_element

            if max_count < k:
                break

            total += N - end
            max_count -= nums[start] == max_element

        return total


assert Solution().countSubarrays([1, 3, 2, 3, 3], 2) == 6
assert Solution().countSubarrays([1, 4, 2, 1], 3) == 0
