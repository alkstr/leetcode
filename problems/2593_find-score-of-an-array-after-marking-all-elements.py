# 2593. Find Score of an Array After Marking All Elements
#
# You are given an array nums consisting of positive integers.
# Starting with score = 0, apply the following algorithm:
# - Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
# - Add the value of the chosen integer to score.
# - Mark the chosen element and its two adjacent elements if they exist.
# - Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        i, n, score = 0, len(nums), 0

        while i < n:
            if i < n - 1 and nums[i] > nums[i + 1]:
                i += 1
                continue

            if i < n - 1:
                nums[i + 1] = 0

            j = i
            while j >= 0 and nums[j] != 0:
                score += nums[j]
                if j > 0:
                    nums[j - 1] = 0
                nums[j] = 0
                j -= 2

            i += 2

        return score


assert Solution().findScore([2, 1, 3, 4, 5, 2]) == 7
assert Solution().findScore([2, 3, 5, 1, 3, 2]) == 5
