# 2235. Add Two Integers
#
# Given two integers num1 and num2, return the sum of the two integers.

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


assert Solution().sum(12, 5) == 17
assert Solution().sum(-10, 4) == -6
