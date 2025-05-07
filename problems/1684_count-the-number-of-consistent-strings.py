# 1684. Count the Number of Consistent Strings
#
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        return sum(all(c in allowed_set for c in word) for word in words)


assert Solution().countConsistentStrings(
    "ab",
    ["ad", "bd", "aaab", "baa", "badab"]
) == 2

assert Solution().countConsistentStrings(
    "abc",
    ["a", "b", "c", "ab", "ac", "bc", "abc"]
) == 7

assert Solution().countConsistentStrings(
    "cad",
    ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
) == 4
