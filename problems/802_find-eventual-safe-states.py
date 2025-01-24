# 802. Find Eventual Safe States
#
# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False for _ in graph]
        stack = [False for _ in graph]

        def dfs(node: int) -> bool:
            if stack[node]:
                return True
            if visited[node]:
                return False

            visited[node] = True

            stack[node] = True
            for adj in graph[node]:
                if dfs(adj):
                    return True
            stack[node] = False

            return False

        for i in range(n):
            dfs(i)

        result = [i for (i, _) in filter(lambda t: not t[1], enumerate(stack))]
        return result


assert Solution().eventualSafeNodes(
    [[1, 2], [2, 3], [5], [0], [5], [], []]
) == [2, 4, 5, 6]

assert Solution().eventualSafeNodes(
    [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
) == [4]
