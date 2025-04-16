# 2537. Count the Number of Good Subarrays
#
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
# A subarray is a contiguous non-empty sequence of elements within an array.

from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def _count_less_than_x(x: int) -> int:
            counter = Counter()
            left, subarrays, pairs = 0, 0, 0
            for right in range(N):
                num = nums[right]
                pairs += counter[num]
                counter[num] += 1

                while pairs >= x:
                    num = nums[left]
                    counter[num] -= 1
                    pairs -= counter[num]
                    left += 1

                subarrays += right - left + 1

            return subarrays

        result = (N + 1) * N // 2 - _count_less_than_x(k)
        return result


assert Solution().countGood([1, 1, 1, 1, 1], 10) == 1
assert Solution().countGood([3, 1, 4, 3, 2, 2, 4], 2) == 4
