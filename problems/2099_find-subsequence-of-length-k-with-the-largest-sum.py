# 2099. Find Subsequence of Length K With the Largest Sum
#
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

import heapq
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        hq = []
        for i, num in enumerate(nums):
            if len(hq) < k:
                heapq.heappush(hq, (num, i))
            elif num > hq[0][0]:
                heapq.heappushpop(hq, (num, i))

        hq.sort(key=lambda t: t[1])
        result = [num for num, _ in hq]
        return result


assert Solution().maxSubsequence([2, 1, 3, 3], 2) == [3, 3]
assert Solution().maxSubsequence([-1, -2, 3, 4], 3) == [-1, 3, 4]
assert Solution().maxSubsequence([3, 4, 3, 3], 2) == [3, 4]
