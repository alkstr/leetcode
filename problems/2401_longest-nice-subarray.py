# 2401. Longest Nice Subarray
#
# You are given an array nums consisting of positive integers.
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
# Return the length of the longest nice subarray.
# A subarray is a contiguous part of an array.
# Note that subarrays of length 1 are always considered nice.


from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        current_bits = nums[0]
        max_len = 1
        left, right = 0, 0

        while left < n:
            if right < n - 1 and nums[right + 1] & current_bits == 0:
                right += 1
                current_bits |= nums[right]
            else:
                current_bits ^= nums[left]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


assert Solution().longestNiceSubarray([1, 4, 8, 5, 2]) == 3

assert Solution().longestNiceSubarray([1, 3, 8, 48, 10]) == 3
assert Solution().longestNiceSubarray([3, 1, 5, 11, 13]) == 1
