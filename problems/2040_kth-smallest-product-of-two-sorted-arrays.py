# 2040. Kth Smallest Product of Two Sorted Arrays
#
# Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the k_th (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def _count_le(n: int) -> int:
            count = 0
            for num in nums1:
                if num > 0:
                    count += bisect_right(nums2, n // num)
                elif num < 0:
                    count += len(nums2) - bisect_left(nums2, -(-n // num))
                elif n >= 0:
                    count += len(nums2)

            return count

        ng, ok = -10 ** 10 - 1, 10 ** 10 + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if _count_le(mid) >= k:
                ok = mid
            else:
                ng = mid

        return ok


assert Solution().kthSmallestProduct([2, 5], [3, 4], 2) == 8
assert Solution().kthSmallestProduct([-4, -2, 0, 3], [2, 4], 6) == 0

assert Solution().kthSmallestProduct(
    [-2, -1, 0, 1, 2],
    [-3, -1, 2, 4, 5],
    3
) == -6
