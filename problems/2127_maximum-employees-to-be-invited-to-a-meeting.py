# 2127. Maximum Employees to Be Invited to a Meeting
#
# A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        reversed_favorite = [[] for _ in favorite]

        for i in range(n):
            reversed_favorite[favorite[i]].append(i)

        max_cycle_len = 0
        duos_len = 0
        visited = [False for _ in favorite]

        for i in range(n):
            if visited[i]:
                continue

            i_to_distance = dict()
            j = i
            distance = 0

            for _ in range(n):
                if visited[j]:
                    break
                visited[j] = True
                i_to_distance[j] = distance
                distance += 1
                next_j = favorite[j]

                if next_j in i_to_distance.keys():
                    cycle_len = distance - i_to_distance[next_j]
                    max_cycle_len = max(max_cycle_len, cycle_len)

                    if cycle_len == 2:
                        chain = set([j, next_j])

                        def bfs(start: int):
                            deq = deque([(start, 0)])
                            max_chain_distance = 0
                            while deq:
                                node, chain_distance = deq.popleft()
                                for neighbor in reversed_favorite[node]:
                                    if neighbor in chain:
                                        continue
                                    chain.add(neighbor)
                                    deq.append(
                                        (neighbor, chain_distance + 1)
                                    )
                                    max_chain_distance = max(
                                        max_chain_distance,
                                        chain_distance + 1
                                    )
                            return max_chain_distance

                        duos_len += (
                            2 + bfs(next_j) + bfs(j)
                        )
                    break
                j = next_j

        return max(max_cycle_len, duos_len)


assert Solution().maximumInvitations([2, 2, 1, 2]) == 3
assert Solution().maximumInvitations([1, 2, 0]) == 3
assert Solution().maximumInvitations([3, 0, 1, 4, 1]) == 4
