# 2900. Longest Unequal Adjacent Groups Subsequence I
#
# You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].
# Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.
# Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i_0, i_1, ..., i_k-1], such that groups[i_j] != groups[i_j+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.
# Return the selected subsequence. If there are multiple answers, return any of them.
# Note: The elements in words are distinct.

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        result = []

        for i in range(N):
            if result and groups[i] == groups[result[-1]]:
                continue

            result.append(i)

        result = [words[i] for i in result]
        return result


assert Solution().getLongestSubsequence(["c"], [0]) == ["c"]
assert Solution().getLongestSubsequence(["d"], [1]) == ["d"]

assert Solution().getLongestSubsequence(
    ["e", "a", "b"],
    [0, 0, 1]
) == ["e", "b"]

assert Solution().getLongestSubsequence(
    ["a", "b", "c", "d"],
    [1, 0, 1, 1]
) == ["a", "b", "c"]
