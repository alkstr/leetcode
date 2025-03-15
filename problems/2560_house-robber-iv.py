# 2560. House Robber IV
#
# There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
# You are given an integer array nums representing how much money is stashed in each house. More formally, the i_th house from the left has nums[i] dollars.
# You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        ng, ok = min(nums) - 1, max(nums) + 1

        def _check(limit: int) -> bool:
            counter = 0
            skip = False
            for num in nums:
                if skip:
                    skip = False
                    continue

                if num <= limit:
                    counter += 1
                    skip = True

                if counter == k:
                    return True

            return False

        def _binary_search():
            nonlocal ng, ok
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if _check(mid):
                    ok = mid
                else:
                    ng = mid

            return ok

        result = _binary_search()
        return result


assert Solution().minCapability([1, 4, 5], 1) == 1

assert Solution().minCapability([2, 3, 5, 9], 2) == 5
assert Solution().minCapability([2, 7, 9, 3, 1], 2) == 2
