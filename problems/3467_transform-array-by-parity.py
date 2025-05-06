# 3467. Transform Array by Parity
#
# You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:
# - Replace each even number with 0.
# - Replace each odd numbers with 1.
# - Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.

from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted(num % 2 for num in nums)


assert Solution().transformArray([4, 3, 2, 1]) == [0, 0, 1, 1]
assert Solution().transformArray([1, 5, 1, 4, 2]) == [0, 0, 1, 1, 1]
