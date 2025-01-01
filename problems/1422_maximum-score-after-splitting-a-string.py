# 1422. Maximum Score After Splitting a String
#
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros, ones = 0, s.count("1")
        result = 0

        for i in range(n - 1):
            char = s[i]

            if char == "0":
                zeros += 1
            else:
                ones -= 1

            result = max(result, zeros + ones)

        return result


assert Solution().maxScore("00") == 1

assert Solution().maxScore("011101") == 5
assert Solution().maxScore("00111") == 5
assert Solution().maxScore("1111") == 3
