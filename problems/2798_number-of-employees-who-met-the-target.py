# 2798. Number of Employees Who Met the Target
#
# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
# The company requires each employee to work for at least target hours.
# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
# Return the integer denoting the number of employees who worked at least target hours.

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)


assert Solution().numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2) == 3
assert Solution().numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6) == 0
