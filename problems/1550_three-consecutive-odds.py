# 1550. Three Consecutive Odds
#
# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(
            i % 2 and j % 2 and k % 2
            for i, j, k
            in zip(arr[:-2], arr[1:-1], arr[2:])
        )


assert not Solution().threeConsecutiveOdds([2, 6, 4, 1])
assert Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
