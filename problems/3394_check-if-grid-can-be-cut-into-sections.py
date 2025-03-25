# 3394. Check if Grid can be Cut into Sections
#
# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [start_x, start_y, end_x, end_y], representing a rectangle on the grid. Each rectangle is defined as follows:
# - (start_x, start_y): The bottom-left corner of the rectangle.
# - (end_x, end_y): The top-right corner of the rectangle.
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:
# - Each of the three resulting sections formed by the cuts contains at least one rectangle.
# - Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.

from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def _check(segs: List[tuple[int, int]]) -> bool:
            first_start = segs[0][0]
            prev_end = segs[0][1]
            count = 0

            for start, end in segs[1:]:
                if start < prev_end:
                    prev_end = max(prev_end, end)
                    continue
                if start != first_start:
                    count += 1
                if count >= 2:
                    return True

                prev_end = end

            return False

        segments = sorted(
            (start_x, end_x)
            for start_x, _, end_x, _
            in rectangles
        )
        if _check(segments):
            return True

        segments = sorted(
            (start_y, end_y)
            for _, start_y, _, end_y
            in rectangles
        )
        if _check(segments):
            return True

        return False


assert Solution().checkValidCuts(
    5,
    [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
)


assert Solution().checkValidCuts(
    4,
    [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]
)

assert not Solution().checkValidCuts(
    4,
    [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]]
)
