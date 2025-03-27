# 2780. Minimum Index of a Valid Split
#
# An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.
# You are given a 0-indexed integer array nums of length n with one dominant element.
# You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:
# - 0 <= i < n - 1
# - nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
# Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.
# Return the minimum index of a valid split. If no valid split exists, return -1.

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        dom = nums[0]
        count = 0
        for num in nums:
            if num == dom:
                count += 1
            else:
                count -= 1
            if count == 0:
                dom = num
                count = 1

        left_dom, right_dom = 0, nums.count(dom)
        for i in range(n - 1):
            if nums[i] == dom:
                left_dom += 1
                right_dom -= 1
            if (left_dom * 2 > i + 1) and (right_dom * 2 > n - i - 1):
                return i

        return -1


assert Solution().minimumIndex([1, 2, 2, 2]) == 2
assert Solution().minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]) == 4
assert Solution().minimumIndex([3, 3, 3, 3, 7, 2, 2]) == -1
