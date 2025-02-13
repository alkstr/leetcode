# 3066. Minimum Operations to Exceed Threshold Value II
#
# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you will:
# - Take the two smallest integers x and y in nums.
# - Remove x and y from nums.
# - Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.
# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hq = [i for i in nums]
        heapq.heapify(hq)
        count = 0

        while hq[0] < k:
            x, y = heapq.heappop(hq), heapq.heappop(hq)
            heapq.heappush(hq, x * 2 + y)
            count += 1

        return count


assert Solution().minOperations([2, 11, 10, 1, 3], 10) == 2
assert Solution().minOperations([1, 1, 2, 4, 9], 20) == 4
