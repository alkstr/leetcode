# 1358. Number of Substrings Containing All Three Characters
#
# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        char_counter = Counter()
        count = 0
        left, right = 0, -1

        while left < n - 1:
            if right < n - 1 and len(char_counter) < 3:
                new_char = s[right+1]
                right += 1
                char_counter[new_char] += 1
            else:
                old_char = s[left]
                left += 1
                char_counter[old_char] -= 1
                if char_counter[old_char] == 0:
                    del char_counter[old_char]

            if len(char_counter) == 3:
                count += n - right

        return count


assert Solution().numberOfSubstrings("abcabc") == 10
assert Solution().numberOfSubstrings("aaacb") == 3
assert Solution().numberOfSubstrings("abc") == 1
