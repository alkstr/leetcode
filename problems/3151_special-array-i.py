# 3151. Special Array I
#
# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return False not in [
            (a % 2) != (b % 2)
            for a, b in zip(nums[:len(nums)-1], nums[1:])
        ]


assert Solution().isArraySpecial([1])
assert Solution().isArraySpecial([2, 1, 4])
assert not Solution().isArraySpecial([4, 3, 1, 6])
