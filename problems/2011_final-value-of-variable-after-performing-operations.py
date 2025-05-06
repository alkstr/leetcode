# 2011. Final Value of Variable After Performing Operations
#
# There is a programming language with only four operations and one variable X:
# - ++X and X++ increments the value of the variable X by 1.
# - --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum({"--X": -1, "X--": -1, "++X": 1, "X++": 1}[op] for op in operations)


assert Solution().finalValueAfterOperations(["--X", "X++", "X++"]) == 1
assert Solution().finalValueAfterOperations(["++X", "++X", "X++"]) == 3
assert Solution().finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0
