# 3108. Minimum Cost Walk in Weighted Graph
#
# There is an undirected weighted graph with n vertices labeled from 0 to n - 1.
# You are given the integer n and an array edges, where edges[i] = [u_i, v_i, w_i] indicates that there is an edge between vertices u_i and v_i with a weight of w_i.
# A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.
# The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w_0, w_1, w_2, ..., w_k, then the cost is calculated as w_0 & w_1 & w_2 & ... & w_k, where & denotes the bitwise AND operator.
# You are also given a 2D array query, where query[i] = [s_i, t_i]. For each query, you need to find the minimum cost of the walk starting at vertex s_i and ending at vertex t_i. If there exists no such walk, the answer is -1.
# Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

from collections import deque
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            i, j, weight = edge
            adj_list[i].append([j, weight, False])
            adj_list[j].append([i, weight, False])

        node_visited = [False for _ in range(n)]
        i_to_root = dict()
        root_to_cost = dict()
        deq = deque()

        for i in range(n):
            if i in i_to_root:
                continue

            node_visited[i] = True
            i_to_root[i] = i
            root_to_cost[i] = 131_071
            deq.append(i)

            while deq:
                current = deq.popleft()
                root = i_to_root[current]
                for edge in adj_list[current]:
                    adj, weight, edge_visited = edge

                    if edge_visited:
                        continue
                    if not node_visited[adj]:
                        node_visited[adj] = True
                        deq.append(adj)

                    edge[2] = True
                    i_to_root[adj] = root
                    root_to_cost[root] &= weight

        result = [None for _ in query]
        for i, q in enumerate(query):
            fr, to = q
            root_fr, root_to = i_to_root[fr], i_to_root[to]
            if root_fr != root_to:
                result[i] = -1
            else:
                result[i] = root_to_cost[root_fr]

        return result


assert Solution().minimumCost(
    7,
    [
        [2, 1, 3], [1, 0, 3], [5, 1, 3], [0, 1, 2],
        [1, 2, 0], [0, 6, 1], [1, 6, 1], [6, 3, 3]
    ],
    [
        [2, 0], [5, 4], [1, 0], [2, 4], [5, 3], [4, 0]
    ],
) == [0, -1, 0, -1, 0, -1]


assert Solution().minimumCost(
    5,
    [[0, 1, 7], [1, 3, 7], [1, 2, 1]],
    [[0, 3], [3, 4]]
) == [1, -1]

assert Solution().minimumCost(
    3,
    [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]],
    [[1, 2]]
) == [0]
