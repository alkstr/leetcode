# 2769. Find the Maximum Achievable Number
#
# Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:
# - Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
# Return the maximum possible value of x.

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


assert Solution().theMaximumAchievableX(4, 1) == 6
assert Solution().theMaximumAchievableX(3, 2) == 7
