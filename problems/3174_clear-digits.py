# 3174. Clear Digits
#
# You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
# - Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        result = deque()
        for c in s:
            if c.isdigit():
                result.pop()
            else:
                result.append(c)

        result = "".join(result)
        return result


assert Solution().clearDigits("abc") == "abc"
assert Solution().clearDigits("cb34") == ""
