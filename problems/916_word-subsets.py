# 916. Word Subsets
#
# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# - For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words1_char_to_count = [dict() for _ in words1]
        words2_char_to_count = [dict() for _ in words2]
        word2_char_to_count = dict()
        result = []

        for i, word in enumerate(words1):
            for c in word:
                if c not in words1_char_to_count[i].keys():
                    words1_char_to_count[i][c] = 0
                words1_char_to_count[i][c] += 1

        for i, word in enumerate(words2):
            for c in word:
                if c not in words2_char_to_count[i].keys():
                    words2_char_to_count[i][c] = 0
                words2_char_to_count[i][c] += 1

        for char_to_count in words2_char_to_count:
            for c, count in char_to_count.items():
                if c not in word2_char_to_count.keys() or word2_char_to_count[c] < count:
                    word2_char_to_count[c] = count

        for i, word1 in enumerate(words1):
            is_universal = True
            for c, count in word2_char_to_count.items():
                if c not in words1_char_to_count[i].keys() or words1_char_to_count[i][c] < count:
                    is_universal = False
                    break

            if is_universal:
                result.append(word1)

        return result


assert Solution().wordSubsets(
    ["amazon", "apple", "facebook", "google", "leetcode"],
    ["lo", "eo"]
) == ["google", "leetcode"]


assert Solution().wordSubsets(
    ["amazon", "apple", "facebook", "google", "leetcode"],
    ["e", "o"]
) == ["facebook", "google", "leetcode"]

assert Solution().wordSubsets(
    ["amazon", "apple", "facebook", "google", "leetcode"],
    ["l", "e"]
) == ["apple", "google", "leetcode"]
