# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
#
# You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count, max_count = 1, 1
        direction = 0

        for i in range(n - 1):
            if nums[i] < nums[i+1]:
                if direction == 1:
                    count += 1
                else:
                    count = 2
                    direction = 1
            elif nums[i] > nums[i+1]:
                if direction == -1:
                    count += 1
                else:
                    count = 2
                    direction = -1
            else:
                count = 1
                direction = 0

            max_count = max(max_count, count)

        return max_count


assert Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2
assert Solution().longestMonotonicSubarray([3, 3, 3, 3]) == 1
assert Solution().longestMonotonicSubarray([3, 2, 1]) == 3
