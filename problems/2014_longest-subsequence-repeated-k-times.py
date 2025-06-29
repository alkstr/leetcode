# 2014. Longest Subsequence Repeated k Times
#
# You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.
# - For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
# Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

from collections import Counter, deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        result = ""
        chars = [char for char, count in Counter(s).items() if count >= k]
        chars.sort(reverse=True)
        deq = deque(chars)

        while deq:
            current_ss = deq.popleft()
            if len(current_ss) > len(result):
                result = current_ss
            for char in chars:
                next_ss = current_ss + char
                iter_s = iter(s)
                if all(char in iter_s for char in next_ss * k):
                    deq.append(next_ss)

        return result


assert Solution().longestSubsequenceRepeatedK("letsleetcode", 2) == "let"
assert Solution().longestSubsequenceRepeatedK("bb", 2) == "b"
assert Solution().longestSubsequenceRepeatedK("ab", 2) == ""
