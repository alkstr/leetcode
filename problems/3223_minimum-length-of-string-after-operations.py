# 3223. Minimum Length of String After Operations
#
# You are given a string s.
# You can perform the following process on s any number of times:
# - Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# - Delete the closest character to the left of index i that is equal to s[i].
# - Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.

class Solution:
    def minimumLength(self, s: str) -> int:
        char_to_count = dict()
        result = 0

        for c in s:
            if c not in char_to_count.keys():
                char_to_count[c] = 0
            char_to_count[c] += 1

        for count in char_to_count.values():
            if count % 2:
                result += 1
            else:
                result += 2

        return result


assert Solution().minimumLength("abaacbcbb") == 5
assert Solution().minimumLength("aa") == 2
