# 1298. Maximum Candies You Can Get from Boxes
#
# You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:
# - status[i] is 1 if the i_th box is open and 0 if the i_th box is closed,
# - candies[i] is the number of candies in the i_th box,
# - keys[i] is a list of the labels of the boxes you can open after opening the i_th box.
# - containedBoxes[i] is a list of the boxes you found inside the i_th box.
# You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
# Return the maximum number of candies you can get following the rules above.

from collections import deque
from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:
        count = 0
        deq = deque()
        current_keys = set()
        current_boxes = set()

        for ib in initialBoxes:
            if status[ib] == 1:
                deq.append(ib)
            else:
                current_boxes.add(ib)

        while deq:
            box = deq.popleft()
            count += candies[box]

            for key in keys[box]:
                current_keys.add(key)
                if key in current_boxes:
                    deq.append(key)
                    current_boxes.remove(key)

            for cb in containedBoxes[box]:
                if status[cb] == 1 or cb in current_keys:
                    deq.append(cb)
                else:
                    current_boxes.add(cb)

        return count


assert Solution().maxCandies(
    [1, 0, 1, 0],
    [7, 5, 4, 100],
    [[], [], [1], []],
    [[1, 2], [3], [], []],
    [0]
) == 16

assert Solution().maxCandies(
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [[1, 2, 3, 4, 5], [], [], [], [], []],
    [[1, 2, 3, 4, 5], [], [], [], [], []],
    [0]
) == 6
