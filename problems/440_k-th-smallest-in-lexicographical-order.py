# 440. K-th Smallest in Lexicographical Order
#
# Given two integers n and k, return the k_th lexicographically smallest integer in the range [1, n].

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        number = 1
        remaining_steps = k - 1

        def _count_steps(fr: int, to: int) -> int:
            steps = 0
            while fr <= n:
                steps += min(n + 1, to) - fr
                fr *= 10
                to *= 10

            return steps

        while remaining_steps > 0:
            step = _count_steps(number, number + 1)
            if step <= remaining_steps:
                number += 1
                remaining_steps -= step
            else:
                number *= 10
                remaining_steps -= 1

        return number


assert Solution().findKthNumber(13, 2) == 10
assert Solution().findKthNumber(1, 1) == 1
