# 2413. Smallest Even Multiple
#
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


assert Solution().smallestEvenMultiple(5) == 10
assert Solution().smallestEvenMultiple(6) == 6
