# 2359. Find Closest Node to Given Two Nodes
#
# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
# You are also given two integers node1 and node2.
# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.
# Note that edges may contain cycles.

from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        INF = 10 ** 6

        dist = [
            [INF for _ in range(N)],
            [INF for _ in range(N)]
        ]

        def _dfs(start: int, i: int):
            dist[i][start] = 0
            deq = deque([start])

            while deq:
                node = deq.pop()
                if edges[node] == -1:
                    continue
                if dist[i][node] < dist[i][edges[node]]:
                    dist[i][edges[node]] = dist[i][node] + 1
                    deq.append(edges[node])

        _dfs(node1, 0)
        _dfs(node2, 1)

        min_i, min_dist = -1, INF
        for i in range(N):
            current_dist = max(dist[0][i], dist[1][i])
            if current_dist < min_dist:
                min_i, min_dist = i, current_dist

        return min_i


assert Solution().closestMeetingNode([2, 2, 3, -1], 0, 1) == 2
assert Solution().closestMeetingNode([1, 2, -1], 0, 2) == 2
