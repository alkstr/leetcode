# 2657. Find the Prefix Common Array of Two Arrays
#
# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        visited = set()
        count = 0
        result = [0 for _ in A]

        for i, (a, b) in enumerate(zip(A, B)):
            if a in visited:
                count += 1
            else:
                visited.add(a)
            if b in visited:
                count += 1
            else:
                visited.add(b)

            result[i] = count

        return result


assert Solution().findThePrefixCommonArray(
    [1, 3, 2, 4],
    [3, 1, 2, 4]
) == [0, 2, 3, 4]

assert Solution().findThePrefixCommonArray([2, 3, 1], [3, 1, 2]) == [0, 1, 3]
