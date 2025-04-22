# 2338. Count the Number of Ideal Arrays
#
# You are given two integers n and maxValue, which are used to describe an ideal array.
# A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
# - Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
# - Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 10^9 + 7.

from math import comb
from functools import lru_cache


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7

        sieve = [0] * (maxValue + 1)
        for i in range(2, maxValue + 1):
            if sieve[i] != 0:
                continue
            for j in range(i, maxValue + 1, i):
                sieve[j] = i

        prime_exponents = [[] for _ in range(maxValue + 1)]
        for i in range(2, maxValue + 1):
            x = i
            while x > 1:
                prime = sieve[x]
                count = 0
                while x % prime == 0:
                    x //= prime
                    count += 1
                prime_exponents[i].append(count)

        @lru_cache(None)
        def binom(a, b):
            return comb(a, b) % MOD

        result = 0
        for val in range(1, maxValue + 1):
            count = 1
            for exp in prime_exponents[val]:
                count = (count * binom(n + exp - 1, exp)) % MOD
            result = (result + count) % MOD

        return result


assert Solution().idealArrays(2, 5) == 10
assert Solution().idealArrays(5, 3) == 11
