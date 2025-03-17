# 2206. Divide Array Into Equal Pairs
#
# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# - Each element belongs to exactly one pair.
# - The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return 1 not in [count % 2 for count in Counter(nums).values()]


assert Solution().divideArray([3, 2, 3, 2, 2, 2])
assert not Solution().divideArray([1, 2, 3, 4])
