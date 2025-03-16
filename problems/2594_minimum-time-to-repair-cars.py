# 2594. Minimum Time to Repair Cars
#
# You are given an integer array ranks representing the ranks of some mechanics. ranks_i is the rank of the i_th mechanic. A mechanic with a rank r can repair n cars in r * n^2 minutes.
# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
# Return the minimum time taken to repair all the cars.
# Note: All the mechanics can repair the cars simultaneously.

from math import sqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def _check(minutes: int) -> bool:
            cars_counter = 0
            for rank in ranks:
                cars_counter += int(sqrt(minutes / rank))
                if cars_counter >= cars:
                    return True

            return False

        def _binary_search(ng: int, ok: int) -> int:
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if _check(mid):
                    ok = mid
                else:
                    ng = mid

            return ok

        result = _binary_search(0, max(ranks) * cars * cars)
        return result


assert Solution().repairCars([4, 2, 3, 1], 10) == 16
assert Solution().repairCars([5, 1, 8], 6) == 16
