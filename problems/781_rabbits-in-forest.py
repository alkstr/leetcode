# 781. Rabbits in Forest
#
# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the i_th rabbit.
# Given the array answers, return the minimum number of rabbits that could be in the forest.

from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        counter = Counter()

        for i in answers:
            counter[i+1] += 1
            if counter[i+1] == i + 1:
                total += i + 1
                counter[i+1] = 0

        for i, count in counter.items():
            if count == 0:
                continue

            total += i

        return total


assert Solution().numRabbits([1, 1, 2]) == 5
assert Solution().numRabbits([10, 10, 10]) == 11
