# 2845. Count of Interesting Subarrays
# You are given a 0-indexed integer array nums, an integer modulo, and an integer k.
# Your task is to find the count of subarrays that are interesting.
# A subarray nums[l..r] is interesting if the following condition holds:
# - Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.
# Return an integer denoting the count of interesting subarrays.
# Note: A subarray is a contiguous non-empty sequence of elements within an array.

from collections import Counter
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        counter = Counter([0])
        total = 0
        prefix = 0
        for num in nums:
            prefix += (num % modulo == k)
            total += counter[(prefix - k + modulo) % modulo]
            counter[prefix % modulo] += 1

        return total


assert Solution().countInterestingSubarrays([3, 2, 4], 2, 1) == 3
assert Solution().countInterestingSubarrays([3, 1, 9, 6], 3, 0) == 2
