# 2929. Distribute Candies Among Children II
#
# You are given two positive integers n and limit.
# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def _calc(n: int) -> int:
            return (
                0
                if n < 0
                else n * (n - 1) // 2
            )

        result = (
            _calc(n + 2)                            # total unrestricted
            - _calc(n - limit + 1) * 3              # at least one exceed limit
            + _calc(n - (limit + 1) * 2 + 2) * 3    # at least two exceed limit
            - _calc(n - (limit + 1) * 3 + 2)        # all three exceed limit
        )
        return result


assert Solution().distributeCandies(5, 2) == 3
assert Solution().distributeCandies(3, 3) == 10
