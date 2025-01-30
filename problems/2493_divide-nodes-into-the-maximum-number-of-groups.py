# 2493. Divide Nodes Into the Maximum Number of Groups
#
# You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.
# You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.
# Divide the nodes of the graph into m groups (1-indexed) such that:
# - Each node in the graph belongs to exactly one group.
# - For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
# Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

from collections import deque
from typing import List


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n + 1)]
        i_to_parent = [-1 for _ in range(n + 1)]
        i_to_depth = [-1 for _ in range(n + 1)]

        def _find(i: int) -> int:
            while i_to_parent[i] != -1:
                i = i_to_parent[i]
            return i

        def _union(i: int, j: int):
            i, j = _find(i), _find(j)
            if i == j:
                return

            if i_to_depth[i] < i_to_depth[j]:
                i, j = j, i
            i_to_parent[j] = i

            if i_to_depth[i] == i_to_depth[j]:
                i_to_depth[i] += 1

        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
            _union(e[0], e[1])

        i_to_groups = dict()

        def _get_groups(i: int):
            i_to_layer = [-1 for _ in range(n + 1)]
            i_to_layer[i] = 0
            deq = deque([i])
            max_layer = 0

            while deq:
                deq_len = len(deq)
                for _ in range(deq_len):
                    node = deq.popleft()
                    for adj in adj_list[node]:
                        if i_to_layer[adj] == -1:
                            i_to_layer[adj] = max_layer + 1
                            deq.append(adj)
                        elif i_to_layer[adj] == max_layer:
                            return -1

                max_layer += 1

            return max_layer

        for i in range(1, n + 1):
            groups = _get_groups(i)
            if groups == -1:
                return -1
            root = _find(i)
            i_to_groups[root] = max(
                i_to_groups.get(root, 0),
                groups
            )

        result = sum(i_to_groups.values())
        return result


assert Solution().magnificentSets(
    6,
    [
        [1, 2],
        [1, 4],
        [1, 5],
        [2, 6],
        [2, 3],
        [4, 6]
    ]
) == 4

assert Solution().magnificentSets(3, [[1, 2], [2, 3], [3, 1]]) == -1
