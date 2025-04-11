# 2843. Count Symmetric Integers
#
# You are given two positive integers low and high.
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
# Return the number of symmetric integers in the range [low, high].

import math


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def _is_symmetric(x: int) -> bool:
            digits_count = math.floor(math.log(x, 10)) + 1
            if digits_count % 2:
                return False

            left_sum, right_sum = 0, 0
            for i in range(digits_count // 2):
                left_sum += (x // 10 ** i) % 10
                right_sum += (x // 10 ** (digits_count - i - 1)) % 10

            return left_sum == right_sum

        return sum(_is_symmetric(i) for i in range(low, high + 1))


assert Solution().countSymmetricIntegers(1, 100) == 9
assert Solution().countSymmetricIntegers(1200, 1230) == 4
