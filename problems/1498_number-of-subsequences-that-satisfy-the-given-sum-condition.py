# 1498. Number of Subsequences That Satisfy the Given Sum Condition
#
# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 10^9 + 7.

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)

        powers_of_two = [1 for _ in range(n + 1)]
        for i in range(1, n + 1):
            powers_of_two[i] = (powers_of_two[i-1] << 1) % MOD

        count = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + powers_of_two[right-left]) % MOD
                left += 1
            else:
                right -= 1

        return count


assert Solution().numSubseq([3, 5, 6, 7], 9) == 4
assert Solution().numSubseq([3, 3, 6, 8], 10) == 6
assert Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
