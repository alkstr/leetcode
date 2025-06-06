# 2434. Using a Robot to Print the Lexicographically Smallest String
#
# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
# - Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# - Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.

from collections import Counter, deque
import string


class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        deq_s = deque(s)
        deq_t = deque()
        result = deque()

        for char in string.ascii_lowercase:
            if char not in counter and (deq_t and deq_t[-1] != char):
                continue

            while deq_t and deq_t[-1] <= char:
                result.append(deq_t.pop())

            while counter[char] > 0:
                current_char = deq_s.popleft()
                counter[current_char] -= 1

                if current_char == char:
                    result.append(current_char)
                else:
                    deq_t.append(current_char)

        while deq_t:
            result.append(deq_t.pop())

        return "".join(result)


assert Solution().robotWithString("zza") == "azz"
assert Solution().robotWithString("bac") == "abc"
assert Solution().robotWithString("bdda") == "addb"
