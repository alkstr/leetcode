# 1752. Check if Array Is Sorted and Rotated
#
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(-1, n-1):
            if nums[i] > nums[i+1]:
                count += 1
            if count == 2:
                return False

        return True


assert Solution().check([3, 4, 5, 1, 2])
assert not Solution().check([2, 1, 3, 4])
assert Solution().check([1, 2, 3])
