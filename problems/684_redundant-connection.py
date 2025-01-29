# 684. Redundant Connection
#
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in edges]

        for t in edges:
            adj_list[t[0]-1].append(t[1]-1)
            adj_list[t[1]-1].append(t[0]-1)

        visited = [False for _ in edges]
        i_to_parent = [-1 for _ in edges]
        cycle_start_ref = [-1]

        def dfs(i: int):
            visited[i] = True

            for adj in adj_list[i]:
                if not visited[adj]:
                    i_to_parent[adj] = i
                    dfs(adj)
                elif adj != i_to_parent[i] and cycle_start_ref[0] == -1:
                    cycle_start_ref[0] = adj
                    i_to_parent[adj] = i

        dfs(0)

        cycle = set()
        cycle_node = cycle_start_ref[0]
        for _ in range(n):
            cycle.add(cycle_node)
            cycle_node = i_to_parent[cycle_node]
            if cycle_node == cycle_start_ref[0]:
                break

        for t in reversed(edges):
            if t[0] - 1 in cycle and t[1] - 1 in cycle:
                return t

        raise Exception("Unreachable")


assert Solution().findRedundantConnection(
    [[1, 2], [1, 3], [2, 3]]
) == [2, 3]

assert Solution().findRedundantConnection(
    [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
) == [1, 4]
