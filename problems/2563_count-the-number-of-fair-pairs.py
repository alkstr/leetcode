# 2563. Count the Number of Fair Pairs
#
# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
# A pair (i, j) is fair if:
# - 0 <= i < j < n, and
# - lower <= nums[i] + nums[j] <= upper

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        nums.sort()

        def _bsearch_left(ng: int, ok: int) -> int:
            i = ng
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if nums[i] + nums[mid] >= lower:
                    ok = mid
                else:
                    ng = mid

            return ok

        def _bsearch_right(ng: int, ok: int) -> int:
            i = ng
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if nums[i] + nums[mid] > upper:
                    ok = mid
                else:
                    ng = mid

            return ok

        count = 0
        for i in range(N - 1):
            count += _bsearch_right(i, N) - _bsearch_left(i, N)

        return count


assert Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6) == 6
assert Solution().countFairPairs([1, 7, 9, 2, 5], 11, 11) == 1
