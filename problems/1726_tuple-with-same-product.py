# 1726. Tuple with Same Product
#
# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_to_freq = dict()
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product not in product_to_freq:
                    product_to_freq[product] = 0
                product_to_freq[product] += 1

        for freq in product_to_freq.values():
            pairs_perms = freq * (freq - 1) // 2
            elements_perms = pairs_perms * 8
            # 8 elements permutations look like this:
            # (a, b) & (c, d) ; (a, c) & (b, d) ; (a, d) & (b, c) ;
            # (c, d) & (a, b) ; (b, d) & (a, c) ; (b, c) & (a, d) .
            count += elements_perms

        return count


assert Solution().tupleSameProduct([2, 3, 4, 6]) == 8
assert Solution().tupleSameProduct([1, 2, 4, 5, 10]) == 16
