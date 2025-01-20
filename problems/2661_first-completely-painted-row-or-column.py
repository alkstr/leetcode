# 2661. First Completely Painted Row or Column
#
# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
# Return the smallest index i at which either a row or a column will be completely painted in mat.

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows, cols = [0 for _ in range(n)], [0 for _ in range(m)]
        num_to_coords = dict()

        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                num_to_coords[num] = (i, j)

        for i, num in enumerate(arr):
            x, y = num_to_coords[num]

            rows[x] += 1
            if rows[x] == m:
                return i

            cols[y] += 1
            if cols[y] == n:
                return i

        raise Exception("Unreachable")


assert Solution().firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]) == 2

assert Solution().firstCompleteIndex(
    [2, 8, 7, 4, 1, 3, 5, 6, 9],
    [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
) == 3
