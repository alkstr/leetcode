# 3272. Find the Count of Good Integers
#
# You are given two positive integers n and k.
# An integer x is called k-palindromic if:
# - x is a palindrome.
# - x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.
# Return the count of good integers containing n digits.
# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        k_palindromes = set()
        base = 10 ** ((n - 1) // 2)
        skip = n % 2 == 1

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][1:] if skip else s[::-1]
            palindrome = int(s)
            if palindrome % k:
                continue
            k_palindromes.add("".join(sorted(s)))

        factorials = [factorial(i) for i in range(n + 1)]
        count = 0
        for k_pal in k_palindromes:
            digits = [0 for _ in range(10)]
            for d in k_pal:
                digits[int(d)] += 1
            combinations = (n - digits[0]) * factorials[n - 1]
            for i in digits:
                combinations //= factorials[i]
            count += combinations

        return count


assert Solution().countGoodIntegers(3, 5) == 27
assert Solution().countGoodIntegers(1, 4) == 2
assert Solution().countGoodIntegers(5, 6) == 2468
