# 2799. Count Complete Subarrays in an Array
#
# You are given an array nums consisting of positive integers.
# We call a subarray of an array complete if the following condition is satisfied:
# - The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
# A subarray is a contiguous non-empty part of an array.

from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        NUMS_DISTINCT = len(set(nums))

        total = 0
        counter = Counter()
        distinct = 0
        right = -1
        for left in range(N):
            while right < N - 1 and distinct < NUMS_DISTINCT:
                right += 1
                if counter[nums[right]] == 0:
                    distinct += 1
                counter[nums[right]] += 1

            if distinct < NUMS_DISTINCT:
                break

            total += N - right
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                distinct -= 1

        return total


assert Solution().countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
assert Solution().countCompleteSubarrays([5, 5, 5, 5]) == 10
