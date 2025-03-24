# 3169. Count Days Without Meetings
# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
# Return the count of days when the employee is available for work but no meetings are scheduled.
# Note: The meetings may overlap.

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda arr: (arr[0], arr[1]))

        count = meetings[0][0] - 1
        last_meeting = meetings[0][1]
        for start, end in meetings[1:]:
            if start <= last_meeting:
                last_meeting = max(last_meeting, end)
                continue

            count += start - last_meeting - 1
            last_meeting = end

        count += days - last_meeting
        return count


assert Solution().countDays(
    57,
    [
        [3, 49], [23, 44], [21, 56], [26, 55],
        [23, 52], [2, 9], [1, 48], [3, 31]
    ]
) == 1

assert Solution().countDays(8, [[3, 4], [4, 8], [2, 5], [3, 8]]) == 1

assert Solution().countDays(10, [[5, 7], [1, 3], [9, 10]]) == 2
assert Solution().countDays(5, [[2, 4], [1, 3]]) == 1
assert Solution().countDays(6, [[1, 6]]) == 0
