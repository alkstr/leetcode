# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for chars in zip(*strs):
            if len(set(chars)) > 1:
                break

            result += chars[0]

        return result


assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
