# 2685. Count the Number of Complete Components
#
# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [a_i, b_i] denotes that there exists an undirected edge connecting vertices a_i and b_i.
# Return the number of complete connected components of the graph.
# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
# A connected component is said to be complete if there exists an edge between every pair of its vertices.

from collections import deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        result = 0
        global_visited = [False for _ in range(n)]
        for i in range(n):
            if global_visited[i]:
                continue
            if len(adj_list[i]) == 0:
                global_visited[i] = True
                result += 1
                continue

            deq = deque([i])
            visited = [False for _ in range(n)]
            global_visited[i], visited[i] = True, True
            count = 0

            while deq:
                current = deq.popleft()
                for adj in adj_list[current]:
                    if visited[adj]:
                        continue

                    global_visited[adj], visited[adj] = True, True
                    count += 1
                    deq.append(adj)

            deq = deque([i])
            visited = [False for _ in range(n)]
            visited[i] = True
            is_complete = True

            while deq:
                current = deq.popleft()
                if len(adj_list[current]) != count:
                    is_complete = False
                    break
                for adj in adj_list[current]:
                    if visited[adj]:
                        continue
                    visited[adj] = True
                    deq.append(adj)

            if is_complete:
                result += 1

        return result


assert Solution().countCompleteComponents(
    6,
    [[0, 1], [0, 2], [1, 2], [3, 4]]
) == 3

assert Solution().countCompleteComponents(
    6,
    [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
) == 1
