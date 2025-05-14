# 3337. Total Characters in String After Transformations II
#
# You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:
# - Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
# - The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
# Return the length of the resulting string after exactly t transformations.
# Since the answer may be very large, return it modulo 10^9 + 7.

from typing import List


class SqMatrix:
    def identity(size: int) -> "SqMatrix":
        matrix = SqMatrix(size)
        for i in range(size):
            matrix.val[i][i] = 1

        return matrix

    def __init__(self, size: int):
        self.size = size
        self.val = [[0] * size for _ in range(size)]

    def mult_matrix(self, matrix: "SqMatrix", mod=None) -> "SqMatrix":
        result = SqMatrix(self.size)

        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if mod is None:
                        result.val[i][j] = (
                            result.val[i][j] +
                            self.val[i][k] * matrix.val[k][j]
                        )
                    else:
                        result.val[i][j] = (
                            result.val[i][j] +
                            self.val[i][k] * matrix.val[k][j]
                        ) % mod

        return result

    def mult_int(self, i: int, mod=None) -> "SqMatrix":
        result = SqMatrix.identity(self.size)
        current = self
        while i:
            if i & 1:
                result = result.mult_matrix(current, mod)

            current = current.mult_matrix(current, mod)
            i >>= 1

        return result


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ORD_A = ord("a")
        N = ord("z") - ORD_A + 1

        dp = SqMatrix(N)
        for i in range(N):
            for j in range(1, nums[i] + 1):
                dp.val[(i+j) % N][i] = 1

        result = dp.mult_int(t, MOD)
        counter = [0 for _ in range(26)]
        for char in s:
            counter[ord(char)-ORD_A] += 1

        count = 0
        for i in range(N):
            for j in range(N):
                count = (count + result.val[i][j] * counter[j]) % MOD

        return count


assert Solution().lengthAfterTransformations(
    "abcyy",
    2,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
) == 7

assert Solution().lengthAfterTransformations(
    "azbk",
    1,
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
) == 8
