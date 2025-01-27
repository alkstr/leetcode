# 1462. Course Schedule IV
#
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
# - For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
# Return a boolean array answer, where answer[j] is the answer to the jth query.

from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses_pre = [set() for _ in range(numCourses)]

        for pre in prerequisites:
            courses_pre[pre[1]].add(pre[0])

        prerequisites_matrix = [
            [False for _ in range(numCourses)]
            for _ in range(numCourses)
        ]

        for i in range(numCourses):
            deq = deque([i])
            visited = [False for _ in courses_pre]

            while deq:
                current_i = deq.pop()
                for pre in courses_pre[current_i]:
                    if visited[pre]:
                        continue

                    visited[pre] = True
                    prerequisites_matrix[i][pre] = True
                    deq.append(pre)

        result = [prerequisites_matrix[q[1]][q[0]] for q in queries]
        return result


assert Solution().checkIfPrerequisite(
    2,
    [[1, 0]], [[0, 1], [1, 0]]
) == [False, True]

assert Solution().checkIfPrerequisite(
    2,
    [], [[1, 0], [0, 1]]
) == [False, False]

assert Solution().checkIfPrerequisite(
    3,
    [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]
) == [True, True]
