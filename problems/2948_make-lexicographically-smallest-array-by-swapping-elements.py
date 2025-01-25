# 2948. Make Lexicographically Smallest Array by Swapping Elements
#
# You are given a 0-indexed array of positive integers nums and a positive integer limit.
# In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.
# Return the lexicographically smallest array that can be obtained by performing the operation any number of times.
# An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(nums)
        group_to_indexes = dict()
        num_to_indexes = dict()

        for i, num in enumerate(nums):
            if num not in num_to_indexes:
                num_to_indexes[num] = []
            num_to_indexes[num].append(i)

        i_group = 0
        group_to_indexes[0] = set(num_to_indexes[sorted_nums[0]])
        for i in range(1, n):
            if abs(sorted_nums[i-1] - sorted_nums[i]) <= limit:
                group_to_indexes[i_group].update(
                    num_to_indexes[sorted_nums[i]]
                )
            else:
                i_group += 1
                group_to_indexes[i_group] = set(num_to_indexes[sorted_nums[i]])

        result = [-1 for _ in nums]
        for indexes in group_to_indexes.values():
            values = sorted(nums[i] for i in indexes)
            for i, val in zip(sorted(indexes), values):
                result[i] = val

        return result


assert Solution().lexicographicallySmallestArray(
    [1, 5, 3, 9, 8],
    2
) == [1, 3, 5, 8, 9]

assert Solution().lexicographicallySmallestArray(
    [1, 7, 6, 18, 2, 1],
    3
) == [1, 6, 7, 18, 1, 2]

assert Solution().lexicographicallySmallestArray(
    [1, 7, 28, 19, 10],
    3
) == [1, 7, 28, 19, 10]
