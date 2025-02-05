# 1790. Check if One String Swap Can Make Strings Equal
#
# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        misses = []

        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                misses.append(i)
            if len(misses) > 2:
                return False

        if len(misses) == 0:
            return True
        if len(misses) == 1:
            return False

        i, j = misses[0], misses[1]
        return s1[i] == s2[j] and s1[j] == s2[i]


assert Solution().areAlmostEqual("bank", "kanb")
assert not Solution().areAlmostEqual("attack", "defend")
assert Solution().areAlmostEqual("kelb", "kelb")
