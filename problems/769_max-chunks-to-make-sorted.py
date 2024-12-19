# 769. Max Chunks To Make Sorted
#
# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_value = 0
        chunks = 0

        for i, v in enumerate(arr):
            max_value = max(max_value, v)
            if max_value == i:
                chunks += 1

        return chunks


assert Solution().maxChunksToSorted([4, 3, 2, 1, 0]) == 1
assert Solution().maxChunksToSorted([1, 0, 2, 3, 4]) == 4
