# 2176. Count Equal and Divisible Pairs in an Array
#
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i, num_1 in enumerate(nums):
            for j, num_2 in enumerate(nums[i+1:], start=i+1):
                if num_1 != num_2 or i * j % k:
                    continue
                count += 1

        return count


assert Solution().countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4
assert Solution().countPairs([1, 2, 3, 4], 1) == 0
