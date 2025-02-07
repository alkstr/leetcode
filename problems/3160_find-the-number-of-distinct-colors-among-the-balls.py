# 3160. Find the Number of Distinct Colors Among the Balls
#
# You are given an integer limit and a 2D array queries of size n x 2.
# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
# Note that when answering a query, lack of a color will not be considered as a color.

from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors_count = defaultdict(int)
        indexes_color = dict()
        result = []

        for index, new_color in queries:
            if index in indexes_color:
                prev_color = indexes_color[index]
                colors_count[prev_color] -= 1
                if colors_count[prev_color] == 0:
                    del colors_count[prev_color]

            indexes_color[index] = new_color
            colors_count[new_color] += 1

            result.append(len(colors_count))

        return result


assert Solution().queryResults(
    4,
    [[1, 4], [2, 5], [1, 3], [3, 4]]
) == [1, 2, 2, 3]

assert Solution().queryResults(
    4,
    [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
) == [1, 2, 2, 3, 4]
