# 2570. Merge Two 2D Arrays by Summing Values
#
# You are given two 2D integer arrays nums1 and nums2.
# - nums1[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
# - nums2[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
# Each array contains unique ids and is sorted in ascending order by id.
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
# - Only ids that appear in at least one of the two arrays should be included in the resulting array.
# - Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n_1, n_2 = len(nums1), len(nums2)
        i_1, i_2 = 0, 0
        nums = []

        while i_1 < n_1 and i_2 < n_2:
            id_1, val_1 = nums1[i_1]
            id_2, val_2 = nums2[i_2]

            if id_1 == id_2:
                nums.append([id_1, val_1 + val_2])
                i_1 += 1
                i_2 += 1
            elif id_1 < id_2:
                nums.append([id_1, val_1])
                i_1 += 1
            else:
                nums.append([id_2, val_2])
                i_2 += 1

        while i_1 < n_1:
            id_1, val_1 = nums1[i_1]
            nums.append([id_1, val_1])
            i_1 += 1

        while i_2 < n_2:
            id_2, val_2 = nums2[i_2]
            nums.append([id_2, val_2])
            i_2 += 1

        return nums


assert Solution().mergeArrays(
    [[1, 2], [2, 3], [4, 5]],
    [[1, 4], [3, 2], [4, 1]]
) == [[1, 6], [2, 3], [3, 2], [4, 6]]

assert Solution().mergeArrays(
    [[2, 4], [3, 6], [5, 5]],
    [[1, 3], [4, 3]]
) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
