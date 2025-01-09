# 2185. Counting Words With a Given Prefix
#
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)


assert Solution().prefixCount(
    ["pay", "attention", "practice", "attend"], "at"
) == 2

assert Solution().prefixCount(
    ["leetcode", "win", "loops", "success"], "code"
) == 0
