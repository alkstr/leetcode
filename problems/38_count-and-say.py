# 38. Count and Say
#
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# - countAndSay(1) = "1"
# - countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
# Given a positive integer n, return the nth element of the count-and-say sequence.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = "1"
        for _ in range(n - 1):
            rle = ""
            last_char = s[0]
            last_char_count = 1
            for char in s[1:]:
                if char == last_char:
                    last_char_count += 1
                    continue

                rle += str(last_char_count) + last_char
                last_char = char
                last_char_count = 1

            rle += str(last_char_count) + last_char
            s = rle

        return s


assert Solution().countAndSay(4) == "1211"
assert Solution().countAndSay(1) == "1"
