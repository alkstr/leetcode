# 2683. Neighboring Bitwise XOR
#
# A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in a binary array original of length n.
# Specifically, for each index i in the range [0, n - 1]:
# - If i = n - 1, then derived[i] = original[i] ⊕ original[0].
# - Otherwise, derived[i] = original[i] ⊕ original[i + 1].
# Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived.
# Return true if such an array exists or false otherwise.
# - A binary array is an array containing only 0's and 1's

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if n == 1:
            return derived[0] == 0

        current = 0

        for i in derived[:n-1]:
            if (i == 0 and current == 0) or (i == 1 and current == 1):
                current = 0
            else:
                current = 1

        return (derived[-1] == 1 and current == 1) or (derived[-1] == 0 and current == 0)


assert Solution().doesValidArrayExist([1, 1, 0])
assert Solution().doesValidArrayExist([1, 1])
assert not Solution().doesValidArrayExist([1, 0])
