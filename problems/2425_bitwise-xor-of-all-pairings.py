# 2425. Bitwise XOR of All Pairings
#
# You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).
# Return the bitwise XOR of all integers in nums3.

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_1, xor_2 = 0, 0

        if len(nums2) % 2:
            for i in nums1:
                xor_1 ^= i

        if len(nums1) % 2:
            for i in nums2:
                xor_2 ^= i

        return xor_1 ^ xor_2


assert Solution().xorAllNums([2, 1, 3], [10, 2, 5, 0]) == 13
assert Solution().xorAllNums([1, 2], [3, 4]) == 0
