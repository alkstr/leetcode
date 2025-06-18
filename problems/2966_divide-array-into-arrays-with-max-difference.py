# 2966. Divide Array Into Arrays With Max Difference
#
# You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.
# Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:
# - The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        for i in range(len(nums) // 3):
            if (
                nums[i*3+2] - nums[i*3+1] > k
                or nums[i*3+2] - nums[i*3] > k
                or nums[i*3+1] - nums[i*3] > k
            ):
                return []

        result = [
            [nums[i*3], nums[i*3+1], nums[i*3+2]]
            for i
            in range(len(nums) // 3)
        ]
        return result


assert Solution().divideArray(
    [1, 3, 4, 8, 7, 9, 3, 5, 1],
    2
) == [
    [1, 1, 3], [3, 4, 5], [7, 8, 9]
]

assert Solution().divideArray([2, 4, 2, 2, 5, 2], 2) == []

assert Solution().divideArray(
    [4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11],
    14
) == [
    [2, 2, 2], [4, 5, 5], [5, 5, 7], [7, 8, 8], [9, 9, 10], [11, 12, 12]
]
