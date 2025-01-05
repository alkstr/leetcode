# 2381. Shifting Letters II
#
# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
# Return the final string after all such shifts to s are applied.

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0 for _ in range(n)]

        for d in shifts:
            start, end, direction = d[0], d[1], d[2]

            if direction == 0:
                diff[start] -= 1
                if (end + 1) <= (n - 1):
                    diff[end + 1] += 1
            else:
                diff[start] += 1
                if (end + 1) <= (n - 1):
                    diff[end + 1] -= 1

        result = [ord(c) - 97 for c in s]
        current_diff = 0
        for i, d in enumerate(diff):
            current_diff += d
            result[i] = (result[i] + current_diff % 26) % 26
            if result[i] < 0:
                result[i] = 26 - result[i]

        result = "".join([chr(c + 97) for c in result])

        return result


assert Solution().shiftingLetters(
    "abc",
    [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"

assert Solution().shiftingLetters(
    "dztz",
    [[0, 0, 0], [1, 1, 1]]) == "catz"
