# 2824. Count Pairs Whose Sum is Less than Target
#
# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()

        count = 0
        right = 0
        for left in range(N - 1):
            right = max(left + 1, right)

            while right < N - 1 and nums[left] + nums[right] < target:
                right += 1
            while right > left + 1 and nums[left] + nums[right] >= target:
                right -= 1

            count += right - left if nums[left] + nums[right] < target else 0

        return count


assert Solution().countPairs([-1, 1, 2, 3, 1], 2) == 3
assert Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2) == 10
