# 2460. Apply Operations to an Array
#
# You are given a 0-indexed array nums of size n consisting of non-negative integers.
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:
# - If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
# After performing all the operations, shift all the 0's to the end of the array.
# - For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
# Return the resulting array.
# Note that the operations are applied sequentially, not all at once.

from typing import List, Optional


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i, j in zip(range(0, n - 1), range(1, n)):
            if nums[i] != nums[j]:
                continue
            nums[i], nums[j] = nums[i] * 2, 0

        def _find_next_zero_index(start: int) -> Optional[int]:
            for i, num in enumerate(nums[start:], start=start):
                if num == 0:
                    return i

            return None

        current_zero_index = _find_next_zero_index(0)
        if current_zero_index is None:
            return nums

        for i, num in enumerate(nums[current_zero_index+1:], start=current_zero_index+1):
            if num == 0:
                continue
            nums[current_zero_index], nums[i] = nums[i], nums[current_zero_index]

            current_zero_index = _find_next_zero_index(current_zero_index)
            if current_zero_index is None:
                break

        return nums


assert Solution().applyOperations(
    [847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]
) == [1694, 399, 832, 1758, 412, 206, 272, 0, 0, 0, 0, 0, 0, 0]

assert Solution().applyOperations([1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]
assert Solution().applyOperations([0, 1]) == [1, 0]
