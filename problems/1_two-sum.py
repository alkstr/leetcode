# 1. Two Sum
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i, item in enumerate(nums):
            if target - item in num_to_index.keys():
                return [num_to_index[target - item], i]
            num_to_index[item] = i

        raise Exception("Unreachable")


assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
assert Solution().twoSum([3, 3], 6) == [0, 1]
