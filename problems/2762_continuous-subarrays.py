# 2762. Continuous Subarrays
#
# You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:
# Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
# Return the total number of continuous subarrays.
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List


def get_subarrays_count(n: int) -> int:
    return n * (n + 1) // 2


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        left = right = 0
        min_num = max_num = nums[0]

        for right in range(n):
            min_num = min(min_num, nums[right])
            max_num = max(max_num, nums[right])

            if max_num - min_num > 2:
                count += get_subarrays_count(right - left)
                left = right
                min_num = max_num = nums[right]

                while abs(nums[left] - min_num) <= 2 and abs(nums[left] - max_num) <= 2:
                    min_num = min(min_num, nums[left])
                    max_num = max(max_num, nums[left])
                    left -= 1

                left += 1
                count -= get_subarrays_count(right - left)

        count += get_subarrays_count(right - left + 1)

        return count


assert Solution().continuousSubarrays([5, 4, 2, 4]) == 8
assert Solution().continuousSubarrays([1, 2, 3]) == 6

assert Solution().continuousSubarrays([1]) == 1
assert Solution().continuousSubarrays([1, 1]) == 3
assert Solution().continuousSubarrays([1, 5]) == 2
assert Solution().continuousSubarrays([42, 41, 42, 41, 41, 40, 39, 38]) == 28
