# 594. Longest Harmonious Subsequence
#
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)

        count = 0
        for num in counter:
            if num + 1 in counter:
                count = max(count, counter[num] + counter[num+1])

        return count


assert Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
assert Solution().findLHS([1, 2, 3, 4]) == 2
assert Solution().findLHS([1, 1, 1, 1]) == 0
