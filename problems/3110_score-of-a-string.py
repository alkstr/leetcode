# 3110. Score of a String
#
# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(x - y) for x, y in zip([ord(c) for c in s[:-1]], [ord(c) for c in s[1:]]))


assert Solution().scoreOfString("hello") == 13
assert Solution().scoreOfString("zaz") == 50
