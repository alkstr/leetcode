# 2818. Apply Operations to Maximize Score
#
# You are given an array nums of n positive integers and an integer k.
# Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:
# - Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
# - Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
# - Multiply your score by x.
# Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.
# The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.
# Return the maximum possible score after applying at most k operations.
# Since the answer may be large, return it modulo 10^9 + 7.


from collections import deque
from math import sqrt
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7

        def _sieve_primes(n: int) -> List[int]:
            sieve = [True for _ in range(n + 1)]
            primes = []
            for num in range(2, n + 1):
                if not sieve[num]:
                    continue
                primes.append(num)
                for mult in range(num * num, n + 1, num):
                    sieve[mult] = False

            return primes

        PRIMES = _sieve_primes(max(nums))

        def _calculate_factor(n: int) -> int:
            factor = 0

            for prime in PRIMES:
                if prime * prime > n:
                    break
                if n % prime != 0:
                    continue

                factor += 1
                while n % prime == 0:
                    n //= prime

            if n > 1:
                factor += 1

            return factor

        num_to_factor = {num: _calculate_factor(num) for num in set(nums)}

        prev_dom = [-1 for _ in nums]
        next_dom = [N for _ in nums]
        deq = deque()

        for i in range(N):
            while deq and num_to_factor[nums[deq[-1]]] < num_to_factor[nums[i]]:
                next_dom[deq.pop()] = i
            if deq:
                prev_dom[i] = deq[-1]

            deq.append(i)

        subarray_count = [
            (next_dom[i] - i) * (i - prev_dom[i]) for i in range(N)
        ]

        def _pow(base: int, exp: int) -> int:
            result = 1

            while exp > 0:
                if exp % 2:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2

            return result

        sorted_nums = sorted(enumerate(nums), key=lambda x: -x[1])
        score = 1
        index = 0
        while k > 0:
            i, num = sorted_nums[index]
            index += 1

            ops = min(k, subarray_count[i])
            score = (score * _pow(num, ops)) % MOD

            k -= ops

        return score


assert Solution().maximumScore([8, 3, 9, 3, 8], 2) == 81
assert Solution().maximumScore([19, 12, 14, 6, 10, 18], 3) == 4788
