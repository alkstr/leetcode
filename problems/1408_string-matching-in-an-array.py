# 1408. String Matching in an Array
#
# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string

from typing import List


def lps(s: str) -> List[int]:
    n = len(s)
    i, length = 1, 0
    result = [0 for _ in s]

    while i < n:
        if s[i] == s[length]:
            length += 1
            result[i] = length
            i += 1
        elif length > 0:
            length = result[length-1]
        else:
            i += 1

    return result


def is_substring_kmp(s: str, ss: str, lps_s: List[int]) -> bool:
    n_s, n_ss = len(s), len(ss)
    i_s, i_ss = 0, 0

    if n_s < n_ss:
        return False

    while i_s < n_s:
        if s[i_s] == ss[i_ss]:
            i_s, i_ss = i_s + 1, i_ss + 1
            if i_ss == n_ss:
                return True
        elif i_ss > 0:
            i_ss = lps_s[i_ss - 1]
        else:
            i_s += 1

    return False


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()

        for i, word in enumerate(words):
            lps_word = lps(word)
            for j, ss in enumerate(words):
                if i == j:
                    continue
                if is_substring_kmp(word, ss, lps_word):
                    result.add(ss)

        return list(result)


assert Solution().stringMatching(
    ["mass", "as", "hero", "superhero"]
) == list(set(["as", "hero"]))

assert Solution().stringMatching(
    ["leetcode", "et", "code"]
) == list(set(["et", "code"]))

assert Solution().stringMatching(
    ["blue", "green", "bu"]
) == []
