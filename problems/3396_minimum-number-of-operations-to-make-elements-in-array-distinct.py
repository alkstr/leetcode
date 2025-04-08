# 3396. Minimum Number of Operations to Make Elements in Array Distinct
#
# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
# - Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.

from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        counter = Counter(nums)
        repeated_count = sum(x > 1 for x in counter.values())
        if repeated_count == 0:
            return 0

        result = 0
        for i in range(0, N, 3):
            for j in range(i, min(i + 3, N)):
                counter[nums[j]] -= 1
                if counter[nums[j]] == 1:
                    repeated_count -= 1
            result += 1
            if repeated_count == 0:
                return result

        return result


assert Solution().minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]) == 2
assert Solution().minimumOperations([4, 5, 6, 4, 4]) == 2
assert Solution().minimumOperations([6, 7, 8, 9]) == 0
