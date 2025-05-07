# 2942. Find Words Containing Character
#
# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order.

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, s in enumerate(words) if x in s]


assert Solution().findWordsContaining(
    ["leet", "code"],
    "e"
) == [0, 1]

assert Solution().findWordsContaining(
    ["abc", "bcd", "aaaa", "cbc"],
    "a"
) == [0, 2]

assert Solution().findWordsContaining(
    ["abc", "bcd", "aaaa", "cbc"],
    "z"
) == []
