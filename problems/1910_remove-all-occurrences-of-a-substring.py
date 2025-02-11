# 1910. Remove All Occurrences of a Substring
#
# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
# - Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.

from collections import deque
from typing import List


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n, part_n = len(s), len(part)

        def _lps(s: str) -> List[int]:
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

        lps = _lps(part)
        deq = deque()
        matching = [0 for _ in range(n + 1)]

        s_i = 0
        part_i = 0
        while s_i < len(s):
            char = s[s_i]
            deq.append(char)

            if char == part[part_i]:
                part_i += 1
                matching[len(deq)] = part_i

                if part_i == part_n:
                    for _ in range(part_n):
                        deq.pop()
                    part_i = 0 if not deq else matching[len(deq)]
            else:
                if part_i != 0:
                    s_i -= 1
                    part_i = lps[part_i - 1]
                    deq.pop()
                else:
                    matching[len(deq)] = 0

            s_i += 1

        result = "".join(deq)
        return result


assert Solution().removeOccurrences("daabcbaabcbc", "abc") == "dab"
assert Solution().removeOccurrences("axxxxyyyyb", "xy") == "ab"
