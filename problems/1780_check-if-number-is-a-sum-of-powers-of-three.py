# 1780. Check if Number is a Sum of Powers of Three
#
# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
# An integer y is a power of three if there exists an integer x such that y == 3^x.

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        s = n
        acc = 3 ** 15
        for _ in range(15, -1, -1):
            if s >= acc:
                s -= acc
            if s == 0:
                return True

            acc //= 3

        return False


assert Solution().checkPowersOfThree(12)
assert Solution().checkPowersOfThree(91)
assert not Solution().checkPowersOfThree(21)
