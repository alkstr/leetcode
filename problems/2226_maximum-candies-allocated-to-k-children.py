# 2226. Maximum Candies Allocated to K Children
#
# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
# You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
# Return the maximum number of candies each child can get.

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sorted_candies = sorted(candies, reverse=True)
        result = 0

        def _children_count_for_pile_size(pile_size: int) -> int:
            count = 0
            for pile in sorted_candies:
                count += pile // pile_size
                if count >= k:
                    break
            return count

        def _binary_search():
            nonlocal result
            left, right = 1, sorted_candies[0]
            while left <= right:
                pile_size = (left + right) // 2
                children_count = _children_count_for_pile_size(pile_size)
                if children_count < k:
                    right = pile_size - 1
                elif children_count >= k:
                    left = pile_size + 1
                    result = max(result, pile_size)

        _binary_search()
        return result


assert Solution().maximumCandies([5, 8, 6], 3) == 5
assert Solution().maximumCandies([2, 5], 11) == 0
