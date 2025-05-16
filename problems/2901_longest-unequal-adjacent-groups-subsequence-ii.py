# 2901. Longest Unequal Adjacent Groups Subsequence II
#
# You are given a string array words, and an array groups, both arrays having length n.
# The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.
# You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i_0, i_1, ..., i_k-1] having length k, the following holds:
# - For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[i_j] != groups[i_j+1], for each j where 0 < j + 1 < k.
# - words[i_j] and words[i_j+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
# Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.
# Note: strings in words may be unequal in length.

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)

        def _check(s_1: str, s_2: str) -> bool:
            if len(s_1) != len(s_2):
                return False

            count = 0
            for c_1, c_2 in zip(s_1, s_2):
                count += 1 if c_1 != c_2 else 0
                if count > 1:
                    return False

            return count == 1

        dp = [0 for _ in words]
        prev = [None for _ in words]
        for i in range(N):
            for j in range(i + 1, N):
                if groups[i] == groups[j]:
                    continue
                if not _check(words[i], words[j]):
                    continue
                if dp[i] + 1 > dp[j]:
                    dp[j], prev[j] = dp[i] + 1, i

        max_i, max_len = 0, dp[0]

        for i in range(N):
            if dp[i] > max_len:
                max_i, max_len = i, dp[i]

        result = []
        i = max_i
        while i is not None:
            result.append(words[i])
            i = prev[i]

        result.reverse()
        return result


assert Solution().getWordsInLongestSubsequence(
    ["bab", "dab", "cab"],
    [1, 2, 2]
) == ["bab", "dab"]

assert Solution().getWordsInLongestSubsequence(
    ["a", "b", "c", "d"],
    [1, 2, 3, 4]
) == ["a", "b", "c", "d"]
