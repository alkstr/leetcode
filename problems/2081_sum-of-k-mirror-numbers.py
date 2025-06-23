# 2081. Sum of k-Mirror Numbers
#
# A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.
# - For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
# - On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
# Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def _is_palindrome(num: int) -> bool:
            buffer = []
            while num:
                buffer.append(num % k)
                num //= k

            return buffer == buffer[::-1]

        total = 0
        half_length = 1
        while n:
            start = 10 ** (half_length - 1)
            end = start * 10
            for mid_length in (0, 1):
                for i in range(start, end):
                    half = str(i)
                    if mid_length == 0:
                        s = half + half[-2::-1]
                    else:
                        s = half + half[::-1]

                    num = int(s)
                    if _is_palindrome(num):
                        total += num
                        n -= 1
                    if not n:
                        return total

            half_length += 1

        return total


assert Solution().kMirror(2, 5) == 25
assert Solution().kMirror(3, 7) == 499
assert Solution().kMirror(7, 17) == 20379000
