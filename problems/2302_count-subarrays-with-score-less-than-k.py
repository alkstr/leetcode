# 2302. Count Subarrays With Score Less Than K
# The score of an array is defined as the product of its sum and its length.
# - For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
# Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.
# A subarray is a contiguous sequence of elements within an array.

from typing import Callable, List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)

        prefix_sum = [0 for _ in nums]
        acc = 0
        for i in range(N):
            acc += nums[i]
            prefix_sum[i] = acc

        def _bsearch(ng: int, ok: int, check: Callable[[int], bool]) -> int:
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(mid):
                    ok = mid
                else:
                    ng = mid

            return ok

        def _check(start: int, end: int) -> bool:
            start = max(start, 0)
            end = min(end, N - 1)
            subarr_sum = prefix_sum[end] - \
                (prefix_sum[start-1] if start > 0 else 0)
            return subarr_sum * (end - start + 1) >= k

        count = 0
        for start in range(N):
            end = _bsearch(start - 1, N, lambda i: _check(start, i))
            count += end - start

        return count


assert Solution().countSubarrays([2, 1, 4, 3, 5], 10) == 6
assert Solution().countSubarrays([1, 1, 1], 5) == 5
