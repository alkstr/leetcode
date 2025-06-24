# 2200. Find All K-Distant Indices in an Array
#
# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
# Return a list of all k-distant indices sorted in increasing order.

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)

        dist_right = [0 for _ in nums]
        dist_right[0] = k + 1 if nums[0] == key else 0
        for i in range(1, n):
            if nums[i] == key:
                dist_right[i] = k + 1
            elif dist_right[i-1] > 0:
                dist_right[i] = dist_right[i-1] - 1

        dist_left = [0 for _ in nums]
        dist_left[n-1] = k + 1 if nums[n-1] == key else 0
        for i in range(n - 2, -1, -1):
            if nums[i] == key:
                dist_left[i] = k + 1
            elif dist_left[i+1] > 0:
                dist_left[i] = dist_left[i+1] - 1

        result = [i for i in range(n) if dist_left[i] or dist_right[i]]
        return result


assert Solution().findKDistantIndices(
    [3, 4, 9, 1, 3, 9, 5],
    9,
    1
) == [
    1, 2, 3, 4, 5, 6
]

assert Solution().findKDistantIndices([2, 2, 2, 2, 2], 2, 2) == [0, 1, 2, 3, 4]
