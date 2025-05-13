# 3335. Total Characters in String After Transformations I
#
# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:
# - If the character is 'z', replace it with the string "ab".
# - Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.
# Since the answer may be very large, return it modulo 10^9 + 7.

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        ORD_A, ORD_Z = ord("a"), ord("z")

        counter = [0 for _ in range(ORD_Z - ORD_A + 1)]
        for char in s:
            counter[ord(char) - ORD_A] += 1

        for _ in range(t):
            z_count = counter[ORD_Z - ORD_A]

            for i in range(ORD_Z - ORD_A, 0, -1):
                counter[i-1], counter[i] = 0, counter[i-1]

            counter[0] += z_count
            counter[1] += z_count

        result = 0
        for count in counter:
            result = (result + count) % MOD

        return result


assert Solution().lengthAfterTransformations("abcyy", 2) == 7
assert Solution().lengthAfterTransformations("azbk", 1) == 5
