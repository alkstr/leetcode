# 3042. Count Prefix and Suffix Pairs I
#
# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
# - isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        result = 0

        for i in range(n):
            n_i = len(words[i])
            for j in range(i + 1, n):
                n_j = len(words[j])
                if n_i > n_j:
                    continue

                if words[j][:n_i] == words[i] and words[j][n_j-n_i:] == words[i]:
                    result += 1

        return result


assert Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4
assert Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2
assert Solution().countPrefixSuffixPairs(["abab", "ab"]) == 0
