# 2894. Divisible and Non-divisible Sums Difference
#
# You are given positive integers n and m.
# Define two integers as follows:
# - num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# - num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        first_div = m if m <= n else 0
        last_div = n - (n % m) if m <= n else 0
        n_div = last_div // m

        total = n * (n + 1) // 2
        num_2 = (first_div + last_div) * n_div // 2
        num_1 = total - num_2

        return num_1 - num_2


assert Solution().differenceOfSums(10, 3) == 19
assert Solution().differenceOfSums(5, 6) == 15
assert Solution().differenceOfSums(5, 1) == -15
