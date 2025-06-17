# 3405. Count the Number of Arrays with K Matching Adjacent Elements
#
# You are given three integers n, m, k. A good array arr of size n is defined as follows:
# - Each element in arr is in the inclusive range [1, m].
# - Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
# Return the number of good arrays that can be formed.
# Since the answer may be very large, return it modulo 10^9 + 7.


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        def _pow(x: int, n: int) -> int:
            result = 1
            while n:
                if n & 1:
                    result = result * x % MOD
                x = x * x % MOD
                n >>= 1

            return result

        fact = [0 for _ in range(n)]
        fact[0] = 1
        for i in range(1, n):
            fact[i] = fact[i-1] * i % MOD

        inv_fact = [0 for _ in range(n)]
        inv_fact[n-1] = _pow(fact[n-1], MOD - 2)
        for i in range(n - 1, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        def _comb(n: int, m: int) -> int:
            return fact[n] * inv_fact[m] % MOD * inv_fact[n-m] % MOD

        result = _comb(n - 1, k) * m % MOD * _pow(m - 1, n - k - 1) % MOD
        return result


assert Solution().countGoodArrays(3, 2, 1) == 4
assert Solution().countGoodArrays(4, 2, 2) == 6
assert Solution().countGoodArrays(5, 2, 0) == 2
