# 2131. Longest Palindrome by Concatenating Two Letter Words
#
# You are given an array of strings words. Each element of words consists of two lowercase English letters.
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
# A palindrome is a string that reads the same forward and backward.

from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = 0
        counter = Counter()

        for word in words:
            if counter[word] > 0:
                counter[word] -= 1
                pairs += 1
            else:
                counter[word[::-1]] += 1

        return pairs * 4 + any(word[0] == word[1] and count > 0 for word, count in counter.items()) * 2


assert Solution().longestPalindrome(["lc", "cl", "gg"]) == 6
assert Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8
assert Solution().longestPalindrome(["cc", "ll", "xx"]) == 2
