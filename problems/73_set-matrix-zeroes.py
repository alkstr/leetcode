# 73. Set Matrix Zeroes
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])

        first_row = 0 in matrix[0]
        first_col = False
        for row in range(M):
            if matrix[row][0] == 0:
                first_col = True
                break

        for row in range(1, M):
            for col in range(1, N):
                if matrix[row][col] == 0:
                    matrix[row][0], matrix[0][col] = 0, 0

        for row in range(1, M):
            if matrix[row][0] == 0:
                for col in range(1, N):
                    matrix[row][col] = 0

        for col in range(1, N):
            if matrix[0][col] == 0:
                for row in range(1, M):
                    matrix[row][col] = 0

        if first_row:
            for col in range(N):
                matrix[0][col] = 0

        if first_col:
            for row in range(M):
                matrix[row][0] = 0
