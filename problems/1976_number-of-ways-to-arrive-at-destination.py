# 1976. Number of Ways to Arrive at Destination
# You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
# You are given an integer n and a 2D integer array roads where roads[i] = [u_i, v_i, time_i] means that there is a road between intersections u_i and v_i that takes time_i minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
# Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 10^9 + 7.

from typing import List
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        adj_list = [[] for _ in range(n)]
        for i, j, weight in roads:
            adj_list[i].append((j, weight))
            adj_list[j].append((i, weight))

        hq = [(0, 0)]
        min_dist = [float("inf") for _ in range(n)]
        path_count = [0 for _ in range(n)]
        path_count[0] = 1

        while hq:
            dist, i = heapq.heappop(hq)
            if dist > min_dist[i]:
                continue

            for adj, weight in adj_list[i]:
                if dist + weight < min_dist[adj]:
                    min_dist[adj] = dist + weight
                    path_count[adj] = path_count[i]
                    heapq.heappush(hq, (min_dist[adj], adj))
                elif dist + weight == min_dist[adj]:
                    path_count[adj] = (path_count[adj] + path_count[i]) % MOD

        return path_count[n-1]


assert Solution().countPaths(
    7,
    [
        [0, 6, 7], [0, 1, 2],
        [1, 2, 3],  [1, 3, 3],
        [6, 3, 3], [3, 5, 1],
        [6, 5, 1], [2, 5, 1],
        [0, 4, 5], [4, 6, 2]
    ]
) == 4

assert Solution().countPaths(2, [[1, 0, 10]]) == 1
