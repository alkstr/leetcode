# 3024. Type of Triangle
#
# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.
# - A triangle is called equilateral if it has all sides of equal length.
# - A triangle is called isosceles if it has exactly two sides of equal length.
# - A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if any(side > sum(nums) - side for side in nums):
            return "none"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"

        return "scalene"


assert Solution().triangleType([3, 3, 3]) == "equilateral"
assert Solution().triangleType([3, 4, 5]) == "scalene"
