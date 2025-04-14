# 1534. Count Good Triplets
#
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# - 0 <= i < j < k < arr.length
# - |arr[i] - arr[j]| <= a
# - |arr[j] - arr[k]| <= b
# - |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)

        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, N):
                    count += 1 if \
                        abs(arr[j] - arr[k]) <= b \
                        and abs(arr[i] - arr[k]) <= c \
                        else 0

        return count


assert Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4
assert Solution().countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1) == 0
