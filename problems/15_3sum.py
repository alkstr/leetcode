# 15. 3Sum
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        counter = Counter(nums)
        nums.sort()

        result = set()
        for i in range(N):
            counter[nums[i]] -= 1
            for j in range(i + 1, N):
                target = -(nums[i] + nums[j])

                if target < nums[j]:
                    break
                if counter[target] >= 2 or (counter[target] >= 1 and target != nums[j]):
                    result.add((nums[i], nums[j], target))

        result = [list(triplet) for triplet in result]
        result.reverse()
        return result


assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert Solution().threeSum([0, 1, 1]) == []
assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
