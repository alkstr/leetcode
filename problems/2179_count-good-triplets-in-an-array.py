# 2179. Count Good Triplets in an Array
#
# You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].
# A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2_v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1_x < pos1_y < pos1_z and pos2_x < pos2_y < pos2_z.
# Return the total number of good triplets.

from typing import List


class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]

    def update(self, index: int, delta: int):
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index

        return result


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        num2_to_i = [0 for _ in range(N)]
        for i, num in enumerate(nums2):
            num2_to_i[num] = i

        num2_i_to_num1_i = [0 for _ in range(N)]
        for i, num in enumerate(nums1):
            num2_i_to_num1_i[num2_to_i[num]] = i

        tree = FenwickTree(N)
        result = 0
        for i in range(N):
            num1_i = num2_i_to_num1_i[i]
            left = tree.query(num1_i)
            tree.update(num1_i, 1)
            right = (N - 1 - num1_i) - (i - left)
            result += left * right
        return result


assert Solution().goodTriplets([2, 0, 1, 3], [0, 1, 2, 3]) == 1
assert Solution().goodTriplets([4, 0, 1, 3, 2], [4, 1, 0, 2, 3]) == 4
