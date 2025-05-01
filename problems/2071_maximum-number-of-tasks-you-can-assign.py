# 2071. Maximum Number of Tasks You Can Assign
#
# You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).
# Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.
# Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

from sortedcontainers import SortedList
from typing import Callable, List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        N, M = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def _check(i: int) -> bool:
            current_pills = pills
            current_workers = SortedList(workers[M - i:])
            for j in range(i - 1, -1, -1):
                if current_workers[-1] >= tasks[j]:
                    current_workers.pop()
                    continue
                if current_pills == 0:
                    return False

                worker_i = current_workers.bisect_left(tasks[j] - strength)
                if worker_i == len(current_workers):
                    return False

                current_pills -= 1
                current_workers.pop(worker_i)

            return True

        def _bsearch(ng: int, ok: int, check: Callable[[int], bool]) -> int:
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(mid):
                    ok = mid
                else:
                    ng = mid

            return ok

        count = _bsearch(0, min(M, N) + 1, lambda i: not _check(i)) - 1
        return count


assert Solution().maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1) == 3
assert Solution().maxTaskAssign([5, 4], [0, 0, 0], 1, 5) == 1
assert Solution().maxTaskAssign([10, 15, 30], [0, 10, 10, 10, 10], 3, 10) == 2
