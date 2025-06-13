# 2616. Minimize the Maximum Difference of Pairs
#
# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)

        def _is_enough_pairs(max_diff: int) -> bool:
            pairs = 0
            i = 1
            while i < n and pairs < p:
                if nums[i] - nums[i-1] <= max_diff:
                    pairs += 1
                    i += 2
                else:
                    i += 1

            return pairs >= p

        ng, ok = -1, nums[-1] - nums[0] + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if _is_enough_pairs(mid):
                ok = mid
            else:
                ng = mid

        return ok


assert Solution().minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1
assert Solution().minimizeMax([4, 2, 1, 2], 1) == 0
