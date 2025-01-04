# 1930. Unique Length-3 Palindromic Subsequences
#
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# - For example, "ace" is a subsequence of "abcde".

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = set(list(s))
        char_to_first_and_last = {c: [] for c in chars}
        count = 0

        for i, c in enumerate(s):
            if len(char_to_first_and_last[c]) < 2:
                char_to_first_and_last[c].append(i)
            else:
                char_to_first_and_last[c][1] = i

        for t in char_to_first_and_last.values():
            if len(t) < 2:
                continue

            first, last = t[0], t[1]
            unique_chars = set()
            for i in range(first + 1, last):
                unique_chars.add(s[i])

            count += len(unique_chars)

        return count


assert Solution().countPalindromicSubsequence("aabca") == 3
assert Solution().countPalindromicSubsequence("adc") == 0
assert Solution().countPalindromicSubsequence("bbcbaba") == 4
