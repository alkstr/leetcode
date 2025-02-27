# 873. Length of Longest Fibonacci Subsequence
#
# A sequence x_1, x_2, ..., x_n is Fibonacci-like if:
# - n >= 3
# - x_i + x_i+1 == x_i+2 for all i + 2 <= n
# Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
# A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_len = 0
        num_to_i = {num: i for i, num in enumerate(arr)}
        table = [[0 for _ in arr] for _ in arr]

        for i, num_1 in enumerate(arr[:-1]):
            for j, num_2 in enumerate(arr[i+1:], start=i+1):
                prev = num_2 - num_1
                prev_i = num_to_i.get(prev, None)

                if prev_i is None or prev_i >= i:
                    continue

                table[i][j] = table[prev_i][i] + 1
                max_len = max(max_len, table[i][j])

        return 0 if max_len == 0 else max_len + 2


assert Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5
assert Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3
