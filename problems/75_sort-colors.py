# 75. Sort Colors
#
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[0], count[0] + count[1]):
            nums[i] = 1
        for i in range(count[0] + count[1], sum(count)):
            nums[i] = 2
