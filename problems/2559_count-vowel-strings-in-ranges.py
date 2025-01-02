# 2559. Count Vowel Strings in Ranges
#
# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set(["a", "e", "i", "o", "u"])
        result = [0 for _ in range(len(queries))]

        count = [0 for _ in range(n)]
        temp = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                temp += 1
            count[i] = temp

        for i, t in enumerate(queries):
            start, end = t[0], t[1]
            result[i] = count[end] - (count[start - 1] if start >= 1 else 0)

        return result


assert Solution().vowelStrings(
    ["aba", "bcb", "ece", "aa", "e"],
    [[0, 2], [1, 4], [1, 1]]) == [2, 3, 0]

assert Solution().vowelStrings(
    ["a", "e", "i"],
    [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1]
