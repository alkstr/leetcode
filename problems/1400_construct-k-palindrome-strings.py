# 1400. Construct K Palindrome Strings
#
# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True

        chars_buffer = set()
        pairs = 0
        for c in s:
            if c in chars_buffer:
                chars_buffer.remove(c)
                pairs += 1
            else:
                chars_buffer.add(c)

        return len(chars_buffer) <= k


assert Solution().canConstruct("messi", 3)

assert Solution().canConstruct("annabelle", 2)
assert not Solution().canConstruct("leetcode", 3)
assert Solution().canConstruct("true", 4)
