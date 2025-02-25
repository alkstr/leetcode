# 1524. Number of Sub-arrays With Odd Sum
#
# Given an array of integers arr, return the number of subarrays with an odd sum.
# Since the answer can be very large, return it modulo 10^9 + 7.

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        prefix_sum = 0
        odd_count, even_count = 0, 1

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1

            count %= MOD

        return count


assert Solution().numOfSubarrays([1, 3, 5]) == 4
assert Solution().numOfSubarrays([2, 4, 6]) == 0
assert Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16
