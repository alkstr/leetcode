# 2364. Count Number of Bad Pairs
#
# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums.

from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        offset_to_count = Counter()
        result = 0

        for i, num in enumerate(nums):
            offset = num - i
            result += i - offset_to_count[offset]
            offset_to_count[offset] += 1

        return result


assert Solution().countBadPairs([4, 1, 3, 3]) == 5
assert Solution().countBadPairs([1, 2, 3, 4, 5]) == 0
