# 2311. Longest Binary Subsequence Less Than or Equal to K
#
# You are given a binary string s and a positive integer k.
# Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
# Note:
# - The subsequence can contain leading zeroes.
# - The empty string is considered to be equal to 0.
# - A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count, current = 0, 0
        for i, digit in enumerate(s[::-1]):
            if digit == "0":
                count += 1
            else:
                bit_value = 1 << i
                if current + bit_value <= k:
                    current += bit_value
                    count += 1

        return count


assert Solution().longestSubsequence("1001010", 5) == 5
assert Solution().longestSubsequence("00101001", 1) == 6
