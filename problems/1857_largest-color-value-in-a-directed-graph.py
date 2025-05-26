# 1857. Largest Color Value in a Directed Graph
#
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
# You are given a string colors where colors[i] is a lowercase English letter representing the color of the i_th node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [a_j, b_j] indicates that there is a directed edge from node a_j to node b_j.
# A valid path in the graph is a sequence of nodes x_1 -> x_2 -> x_3 -> ... -> x_k such that there is a directed edge from x_i to x_i+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

from enum import IntEnum
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        class _State(IntEnum):
            NOT_VISITED = 0
            VISITING = 1
            VISITED = 2

        N = len(colors)
        ORD_A, ORD_Z = ord("a"), ord("z")
        COLORS_N = ORD_Z - ORD_A + 1

        state = [_State.NOT_VISITED for _ in colors]
        node_to_colors = [[0 for _ in range(COLORS_N)] for _ in colors]
        adj = [[] for _ in colors]
        for fr, to in edges:
            adj[fr].append(to)

        def _dfs(i: int) -> bool:
            state[i] = _State.VISITING
            for a in adj[i]:
                match state[a]:
                    case _State.NOT_VISITED:
                        if not _dfs(a):
                            return False
                    case _State.VISITING:
                        return False

                for c in range(COLORS_N):
                    node_to_colors[i][c] = max(
                        node_to_colors[i][c],
                        node_to_colors[a][c]
                    )

            node_to_colors[i][ord(colors[i]) - ORD_A] += 1
            state[i] = _State.VISITED
            return True

        for i in range(N):
            if state[i] == _State.VISITED:
                continue
            if not _dfs(i):
                return -1

        result = max(max(node_to_colors[node]) for node in range(N))
        return result


assert Solution().largestPathValue(
    "abaca",
    [[0, 1], [0, 2], [2, 3], [3, 4]]
) == 3

assert Solution().largestPathValue("a", [[0, 0]]) == -1
