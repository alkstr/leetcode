# 3289. The Two Sneaky Numbers of Digitville
#
# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.
# As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()

        def _iter(num: int) -> bool:
            if num in visited:
                return True
            visited.add(num)
            return False

        return sorted(num for num in nums if _iter(num))


assert Solution().getSneakyNumbers([0, 1, 1, 0]) == [0, 1]
assert Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2]) == [2, 3]

assert Solution().getSneakyNumbers(
    [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
) == [4, 5]
