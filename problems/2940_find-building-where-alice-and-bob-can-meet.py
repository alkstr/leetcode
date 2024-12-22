# 2940. Find Building Where Alice and Bob Can Meet
#
# You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
# If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
# You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
# Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

from typing import List
from heapq import heappop, heappush


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        heap_queue = []
        queries_list = [[] for _ in heights]
        result = [-1 for _ in queries]

        for i, query in enumerate(queries):
            a_i, b_i = query
            if a_i > b_i:
                a_i, b_i = b_i, a_i

            if a_i == b_i:
                result[i] = a_i
            elif heights[a_i] < heights[b_i]:
                result[i] = b_i
            else:
                queries_list[max(a_i, b_i)].append(
                    (max(heights[a_i], heights[b_i]), i)
                )

        for i, height in enumerate(heights):
            while heap_queue and heap_queue[0][0] < height:
                _, result_i = heappop(heap_queue)
                result[result_i] = i

            for query in queries_list[i]:
                heappush(heap_queue, query)

        return result


assert Solution().leftmostBuildingQueries(
    [6, 4, 8, 5, 2, 7],
    [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]) == [2, 5, -1, 5, 2]

assert Solution().leftmostBuildingQueries(
    [5, 3, 8, 2, 6, 1, 4, 6],
    [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]) == [7, 6, -1, 4, 6]
