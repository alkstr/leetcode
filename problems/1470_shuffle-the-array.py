# 1470. Shuffle the Array
#
# Given the array nums consisting of 2n elements in the form [x_1,x_2,...,x_n,y_1,y_2,...,y_n].
# Return the array in the form [x_1,y_1,x_2,y_2,...,x_n,y_n].

import itertools
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(itertools.chain.from_iterable(zip(nums[:n], nums[n:])))


assert Solution().shuffle(
    [2, 5, 1, 3, 4, 7],
    3
) == [2, 3, 5, 4, 1, 7]

assert Solution().shuffle(
    [1, 2, 3, 4, 4, 3, 2, 1],
    4
) == [1, 4, 2, 3, 3, 2, 4, 1]

assert Solution().shuffle(
    [1, 1, 2, 2],
    2
) == [1, 2, 1, 2]
