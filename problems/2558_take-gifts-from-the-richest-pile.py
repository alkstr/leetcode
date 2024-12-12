# 2558. Take Gifts From the Richest Pile
#
# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
# - Choose the pile with the maximum number of gifts.
# - If there is more than one pile with the maximum number of gifts, choose any.
# - Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.

from math import sqrt
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # To make "max" heap queue out of min heap, we invert all numbers in list
        gifts = list(map(lambda x: -x, gifts))
        heapify(gifts)
        for _ in range(k):
            max_value = -heappop(gifts)
            heappush(gifts, -int(sqrt(max_value)))

        return -sum(gifts)


assert Solution().pickGifts([25, 64, 9, 4, 100], 4) == 29
assert Solution().pickGifts([1, 1, 1, 1], 4) == 4
