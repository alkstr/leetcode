# 763. Partition Labels
#
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_last_occurence = dict()
        for i, c in enumerate(s):
            char_to_last_occurence[c] = i

        start, end = 0, 0
        current_chars = set()
        result = []
        for i, c in enumerate(s):
            if c not in current_chars:
                current_chars.add(c)
                end = max(end, char_to_last_occurence[c])
            if i == end:
                result.append(end - start + 1)
                start, end = i + 1, i + 1

        return result


assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert Solution().partitionLabels("eccbbbbdec") == [10]
