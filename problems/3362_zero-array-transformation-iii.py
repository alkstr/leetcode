# 3362. Zero Array Transformation III
#
# You are given an integer array nums of length n and a 2D array queries where queries[i] = [l_i, r_i].
# Each queries[i] represents the following action on nums:
# - Decrement the value at each index in the range [l_i, r_i] in nums by at most 1.
# - The amount by which the value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.
# Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

from typing import List
import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        queries.sort(key=lambda q: q[0])

        hq = []
        diffs = [0 for _ in range(N + 1)]
        diff = 0
        q_i = 0

        for i, num in enumerate(nums):
            diff += diffs[i]
            while q_i < len(queries) and queries[q_i][0] == i:
                heapq.heappush(hq, -queries[q_i][1])
                q_i += 1
            while diff < num and hq and -hq[0] >= i:
                diff += 1
                end = -heapq.heappop(hq) + 1
                diffs[end] -= 1
            if diff < num:
                return -1

        return len(hq)


assert Solution().maxRemoval(
    [2, 0, 2],
    [[0, 2], [0, 2], [1, 1]]
) == 1

assert Solution().maxRemoval(
    [1, 1, 1, 1],
    [[1, 3], [0, 2], [1, 3], [1, 2]]
) == 2

assert Solution().maxRemoval([1, 2, 3, 4], [[0, 3]]) == -1
