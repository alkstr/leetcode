# 1512. Number of Good Pairs
#
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum((count - 1) * count // 2 for count in Counter(nums).values())


assert Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
assert Solution().numIdenticalPairs([1, 1, 1, 1]) == 6
assert Solution().numIdenticalPairs([1, 2, 3]) == 0
