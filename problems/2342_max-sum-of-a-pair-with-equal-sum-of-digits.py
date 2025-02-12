# 2342. Max Sum of a Pair With Equal Sum of Digits
#
# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_to_nums = defaultdict(list)

        def _digit_sum(num: int) -> int:
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s

        for num in nums:
            digit_sum = _digit_sum(num)
            heapq.heappush(digit_sum_to_nums[digit_sum], num)
            if len(digit_sum_to_nums[digit_sum]) > 2:
                heapq.heappop(digit_sum_to_nums[digit_sum])

        result = max(
            arr[0] + arr[1]
            if len(arr) == 2
            else -1
            for arr in digit_sum_to_nums.values()
        )
        return result


assert Solution().maximumSum([18, 43, 36, 13, 7]) == 54
assert Solution().maximumSum([10, 12, 19, 14]) == -1
