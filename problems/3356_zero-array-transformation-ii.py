# 3356. Zero Array Transformation II
#
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [l_i, r_i, val_i].
# Each queries[i] represents the following action on nums:
# - Decrement the value at each index in the range [l_i, r_i] in nums by at most val_i.
# - The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.
# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        current_diff = 0
        diff = [0 for _ in range(n + 1)]
        queries_count = 0

        for i, num in enumerate(nums):
            while current_diff + diff[i] < num:
                queries_count += 1

                if queries_count > len(queries):
                    return -1

                left, right, val = queries[queries_count - 1]

                if right >= i:
                    diff[max(left, i)] += val
                    diff[right + 1] -= val

            current_diff += diff[i]

        return queries_count


assert Solution().minZeroArray(
    [2, 0, 2],
    [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
) == 2

assert Solution().minZeroArray(
    [4, 3, 2, 1],
    [[1, 3, 2], [0, 2, 1]]
) == -1
