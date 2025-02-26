# 1749. Maximum Absolute Sum of Any Subarray
#
# You are given an integer array nums. The absolute sum of a subarray [numsl, nums_l+1, ..., nums_r-1, nums_r] is abs(nums_l + nums_l+1 + ... + nums_r-1 + nums_r).
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
# Note that abs(x) is defined as follows:
# - If x is a negative integer, then abs(x) = -x.
# - If x is a non-negative integer, then abs(x) = x.

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        neg_cur, min_sum = nums[0], nums[0]
        pos_cur, max_sum = nums[0], nums[0]

        for num in nums[1:]:
            neg_cur = min(neg_cur + num, num)
            min_sum = min(min_sum, neg_cur)

            pos_cur = max(pos_cur + num, num)
            max_sum = max(max_sum, pos_cur)

        return max(abs(min_sum), abs(max_sum))


assert Solution().maxAbsoluteSum([1, -3, 2, 3, -4]) == 5
assert Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8
