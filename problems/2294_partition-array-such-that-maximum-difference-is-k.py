# 2294. Partition Array Such That Maximum Difference Is K
#
# You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.
# Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] - nums[left] > k:
                count += 1
                left = right

        return count + 1


assert Solution().partitionArray([3, 6, 1, 2, 5], 2) == 2
assert Solution().partitionArray([1, 2, 3], 1) == 2
assert Solution().partitionArray([2, 2, 4, 5], 0) == 3
