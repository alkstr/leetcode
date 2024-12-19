# 1475. Final Prices With a Special Discount in a Shop
#
# You are given an integer array prices where prices[i] is the price of the ith item in a shop.
# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

from collections import deque
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        deq = deque()

        for i, price in enumerate(prices):
            while deq and prices[deq[-1]] >= price:
                result[deq.pop()] -= price

            deq.append(i)

        return result


assert Solution().finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]) == [
    1, 3, 2, 1, 7, 0, 0, 6, 9, 1]

assert Solution().finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
assert Solution().finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert Solution().finalPrices([10, 1, 1, 6]) == [9, 0, 1, 6]
