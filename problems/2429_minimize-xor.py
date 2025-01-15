# 2429. Minimize XOR
#
# Given two positive integers num1 and num2, find the positive integer x such that:
# - x has the same number of set bits as num2, and
# - The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
# Return the integer x. The test cases are generated such that x is uniquely determined.
# The number of set bits of an integer is the number of 1's in its binary representation.

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_bits_count = sum(
            [1 if (num2 & (2 ** i)) else 0 for i in range(32)]
        )
        result, bits = 0, 0

        for i in range(31, -1, -1):
            if num1 & (2 ** i):
                result += 2 ** i
                bits += 1
            if bits == num2_bits_count:
                return result

        for i in range(32):
            if not (result & (2 ** i)):
                result += 2 ** i
                bits += 1
            if bits == num2_bits_count:
                return result

        return result


assert Solution().minimizeXor(3, 5) == 3
assert Solution().minimizeXor(1, 12) == 3
