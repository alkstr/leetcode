# 1295. Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.

from math import log10
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(log10(num)) % 2 for num in nums)


assert Solution().findNumbers([12, 345, 2, 6, 7896]) == 2
assert Solution().findNumbers([555, 901, 482, 1771]) == 1
