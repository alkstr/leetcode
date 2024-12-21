# 2872. Maximum Number of K-Divisible Components
#
# There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.
# A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.
# Return the maximum number of components in any valid split.

from typing import List


def dfs(adj_list: List[List[int]], values: List[int], k: int, parent: int, current: int, count: int):
    s = 0

    for node in adj_list[current]:
        if node == parent:
            continue

        s += dfs(adj_list, values, k, current, node, count)

    s += values[current]

    if not s % k:
        count[0] += 1

    return s


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        count = [0]

        dfs(adj_list, values, k, -1, 0, count)

        return count[0]


assert Solution().maxKDivisibleComponents(
    5,
    [[0, 2], [1, 2], [1, 3], [2, 4]],
    [1, 8, 1, 4, 4], 6) == 2

assert Solution().maxKDivisibleComponents(
    7,
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
    [3, 0, 6, 1, 5, 2, 1], 3) == 3
