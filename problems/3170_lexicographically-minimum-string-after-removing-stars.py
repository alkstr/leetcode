# 3170. Lexicographically Minimum String After Removing Stars
#
# You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.
# While there is a '*', do the following operation:
# - Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
# Return the lexicographically smallest resulting string after removing all '*' characters.

import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        hq = []
        result = list(s)
        for i, char in enumerate(s):
            if char == "*":
                char, char_i = heapq.heappop(hq)
                char_i = -char_i
                result[i], result[char_i] = "", ""
            else:
                heapq.heappush(hq, (char, -i))

        result = "".join(result)
        return result


assert Solution().clearStars("aaba*") == "aab"
assert Solution().clearStars("abc") == "abc"
