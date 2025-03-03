# 2161. Partition Array According to Given Pivot
#
# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
# - Every element less than pivot appears before every element greater than pivot.
# - Every element equal to pivot appears in between the elements less than and greater than pivot.
# - The relative order of the elements less than pivot and the elements greater than pivot is maintained.
#   - More formally, consider every p_i, p_j where p_i is the new position of the i_th element and p_j is the new position of the j_th element. If i < j and both elements are smaller (or larger) than pivot, then p_i < p_j.
# Return nums after the rearrangement.

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal = 0, 0
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1

        result = [None for _ in nums]
        i_less, i_equal, i_greater = 0, less, less + equal
        for num in nums:
            if num < pivot:
                result[i_less] = num
                i_less += 1
            elif num == pivot:
                result[i_equal] = num
                i_equal += 1
            elif num > pivot:
                result[i_greater] = num
                i_greater += 1

        return result


assert Solution().pivotArray(
    [9, 12, 5, 10, 14, 3, 10],
    10
) == [9, 5, 3, 10, 10, 12, 14]

assert Solution().pivotArray(
    [-3, 4, 3, 2],
    2
) == [-3, 2, 4, 3]
