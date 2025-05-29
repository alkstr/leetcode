# 3373. Maximize the Number of Target Nodes After Connecting Trees II
#
# There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i in the first tree and edges2[i] = [u_i, v_i] indicates that there is an edge between nodes u_i and v_i in the second tree.
# Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

from collections import deque
from typing import List, Tuple


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N = max(max(edge) for edge in edges1) + 1
        M = max(max(edge) for edge in edges2) + 1

        adj = [
            [[] for _ in range(N)],
            [[] for _ in range(M)]
        ]
        for node_1, node_2 in edges1:
            adj[0][node_1].append(node_2)
            adj[0][node_2].append(node_1)
        for node_1, node_2 in edges2:
            adj[1][node_1].append(node_2)
            adj[1][node_2].append(node_1)

        colors = [
            [-1 for _ in range(N)],
            [-1 for _ in range(M)]
        ]
        colors[0][0], colors[1][0] = 0, 0

        def _targets(tree: int) -> Tuple[int, int]:
            count = 0
            deq = deque([0])
            while deq:
                node = deq.popleft()
                count += colors[tree][node]

                for a in adj[tree][node]:
                    if colors[tree][a] != -1:
                        continue

                    colors[tree][a] = 0 if colors[tree][node] == 1 else 1
                    deq.append(a)

            return (len(adj[tree]) - count, count)

        tree_0_targets = _targets(0)
        tree_1_max_target = max(_targets(1))
        result = [
            tree_0_targets[colors[0][i]] + tree_1_max_target
            for i in range(N)
        ]
        return result


assert Solution().maxTargetNodes(
    [[0, 1], [0, 2], [2, 3], [2, 4]],
    [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
) == [8, 7, 7, 8, 8]

assert Solution().maxTargetNodes(
    [[0, 1], [0, 2], [0, 3], [0, 4]],
    [[0, 1], [1, 2], [2, 3]]
) == [3, 6, 6, 6, 6]
