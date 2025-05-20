# 3355. Zero Array Transformation I
#
# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [l_i, r_i].
# For each queries[i]:
# - Select a subset of indices within the range [l_i, r_i] in nums.
# - Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.
# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)

        diffs = [0 for _ in range(N + 1)]
        for left, right in queries:
            diffs[left] -= 1
            diffs[right+1] += 1

        diff = 0
        for i, num in enumerate(nums):
            diff += diffs[i]
            if num + diff > 0:
                return False

        return True


assert Solution().isZeroArray([1, 0, 1], [[0, 2]])
assert not Solution().isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]])
