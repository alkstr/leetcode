# 704. Binary Search
#
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

from typing import Callable, List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        def _bsearch(ng: int, ok: int, check: Callable[[int], bool]) -> int:
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(mid):
                    ok = mid
                else:
                    ng = mid

            return ok

        result = _bsearch(-1, N, lambda i: nums[i] >= target)
        if result in (-1, N) or nums[result] != target:
            return -1
        return result


assert Solution().search([-1, 0, 5], -1) == 0

assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
