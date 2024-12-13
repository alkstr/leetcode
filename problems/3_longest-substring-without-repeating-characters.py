# 3. Longest Substring Without Repeating Characters
#
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        char_to_count = dict([(c, 0) for c in set(s)])
        left, right = 0, 0
        max_len = 1
        n = len(s)

        char_to_count[s[left]] += 1
        while right < n - 1:
            right += 1
            char_to_count[s[right]] += 1
            while char_to_count[s[right]] > 1:
                char_to_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3

assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring("a") == 1
