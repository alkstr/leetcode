# 3442. Maximum Difference Between Even and Odd Frequency I
#
# You are given a string s consisting of lowercase English letters.
# Your task is to find the maximum difference diff = freq(a_1) - freq(a_2) between the frequency of characters a_1 and a_2 in the string such that:
# - a_1 has an odd frequency in the string.
# - a_2 has an even frequency in the string.
# Return this maximum difference.

import string


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [s.count(char) for char in string.ascii_lowercase]
        freq = [cnt for cnt in freq if cnt > 0]
        freq.sort()

        max_odd = next(cnt for cnt in reversed(freq) if cnt % 2 == 1)
        min_even = next(cnt for cnt in freq if cnt % 2 == 0)

        result = max_odd - min_even
        return result


assert Solution().maxDifference("aaaaabbc") == 3
assert Solution().maxDifference("abcabcab") == 1
