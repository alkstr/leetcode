# 3343. Count Number of Balanced Permutations
#
# You are given a string num. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of the digits at odd indices.
# Return the number of distinct permutations of num that are balanced.
# Since the answer may be very large, return it modulo 10^9 + 7.
# A permutation is a rearrangement of all the characters of a string.

from math import comb


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        N = len(num)

        digit_sum = sum(int(digit) for digit in num)
        if digit_sum % 2:
            return 0

        TARGET = digit_sum // 2
        MAX_ODD_COUNT = (N + 1) // 2

        digit_count = [num.count(str(i)) for i in range(10)]
        dp = [
            [0 for _ in range(MAX_ODD_COUNT + 1)]
            for _ in range(TARGET + 1)
        ]
        dp[0][0] = 1
        first_i_digits_count = 0
        first_i_digits_sum = 0
        for i in range(10):
            first_i_digits_count += digit_count[i]
            first_i_digits_sum += i * digit_count[i]

            for odd_count in range(
                min(first_i_digits_count, MAX_ODD_COUNT),
                max(0, first_i_digits_count - (N - MAX_ODD_COUNT)) - 1,
                -1
            ):
                even_count = first_i_digits_count - odd_count
                for current in range(
                    min(first_i_digits_sum, TARGET),
                    max(0, first_i_digits_sum - TARGET) - 1,
                    -1
                ):
                    result = 0
                    for j in range(
                        max(0, digit_count[i] - even_count),
                        min(digit_count[i], odd_count) + 1
                    ):
                        if i * j > current:
                            break

                        ways = (
                            comb(odd_count, j)
                            * comb(even_count, digit_count[i] - j) % MOD
                        )
                        result = (
                            result + ways
                            * dp[current-i*j][odd_count-j] % MOD
                        ) % MOD

                    dp[current][odd_count] = result % MOD

        return dp[TARGET][MAX_ODD_COUNT]


assert Solution().countBalancedPermutations("123") == 2
assert Solution().countBalancedPermutations("112") == 1
assert Solution().countBalancedPermutations("12345") == 0
