# 2523. Closest Prime Numbers in Range
#
# Given two positive integers left and right, find the two integers num1 and num2 such that:
# - left <= num1 < num2 <= right.
# - Both num1 and num2 are prime numbers.
# - num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

from math import sqrt
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True for _ in range(right + 1)]
        sieve[0], sieve[1] = False, False

        start, end = 2, int(sqrt(right))
        for i in range(start, end + 1):
            if not sieve[i]:
                continue

            for j in range(i*i, right + 1, i):
                sieve[j] = False

        result = [-1, -1]
        prev, curr = None, None
        for i in range(left, right + 1):
            if not sieve[i]:
                continue

            prev, curr = curr, i

            if prev is None:
                continue
            if result == [-1, -1] or curr - prev < result[1] - result[0]:
                result = [prev, curr]

        return result


assert Solution().closestPrimes(1, 1000000) == [2, 3]

assert Solution().closestPrimes(10, 19) == [11, 13]
assert Solution().closestPrimes(4, 6) == [-1, -1]
