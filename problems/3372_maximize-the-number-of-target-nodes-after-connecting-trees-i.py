# 3372. Maximize the Number of Target Nodes After Connecting Trees I
#
# There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.
# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [a_i, b_i] indicates that there is an edge between nodes a_i and b_i in the first tree and edges2[i] = [u_i, v_i] indicates that there is an edge between nodes u_i and v_i in the second tree. You are also given an integer k.
# Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.
# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.
# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

from collections import deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
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

        def _score(tree: int, max_steps: int, start: int) -> int:
            visited = set([start])
            score = 0
            deq = deque([(start, 0)])
            while deq:
                node, step = deq.popleft()
                if step > max_steps:
                    continue

                score += 1
                for a in adj[tree][node]:
                    if a in visited:
                        continue
                    visited.add(a)
                    deq.append((a, step + 1))

            return score

        tree_1_max = max(_score(1, k - 1, i) for i in range(M))
        result = [_score(0, k, i) + tree_1_max for i in range(N)]
        return result


assert Solution().maxTargetNodes(
    [[0, 1], [0, 2], [2, 3], [2, 4]],
    [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
    2
) == [9, 7, 9, 8, 8]

assert Solution().maxTargetNodes(
    [[0, 1], [0, 2], [0, 3], [0, 4]],
    [[0, 1], [1, 2], [2, 3]],
    1
) == [6, 3, 3, 3, 3]
