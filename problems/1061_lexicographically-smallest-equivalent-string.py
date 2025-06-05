# 1061. Lexicographically Smallest Equivalent String
#
# You are given two strings of the same length s1 and s2 and a string baseStr.
# We say s1[i] and s2[i] are equivalent characters.
# - For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:
# - Reflexivity: 'a' == 'a'.
# - Symmetry: 'a' == 'b' implies 'b' == 'a'.
# - Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

import string


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ORD_A = ord("a")
        char_to_smallest = list(string.ascii_lowercase)

        for char_1, char_2 in zip(s1, s2):
            new_smallest, old_smallest = sorted(
                (
                    char_to_smallest[ord(char_1)-ORD_A],
                    char_to_smallest[ord(char_2)-ORD_A]
                )
            )

            for i, c in enumerate(char_to_smallest):
                if c == old_smallest:
                    char_to_smallest[i] = new_smallest

        result = "".join(char_to_smallest[ord(char)-ORD_A] for char in baseStr)
        return result


assert Solution().smallestEquivalentString(
    "parker",
    "morris",
    "parser"
) == "makkek"

assert Solution().smallestEquivalentString(
    "hello",
    "world",
    "hold"
) == "hdld"

assert Solution().smallestEquivalentString(
    "leetcode",
    "programs",
    "sourcecode"
) == "aauaaaaada"
