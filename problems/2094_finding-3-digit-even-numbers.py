# 2094. Finding 3-Digit Even Numbers
#
# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
# You need to find all the unique integers that follow the given requirements:
# - The integer consists of the concatenation of three elements from digits in any arbitrary order.
# - The integer does not have leading zeros.
# - The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
# Return a sorted array of the unique integers.

from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(digits)

        def _filter(num: int) -> bool:
            num_str = str(num)
            num_counter = Counter(int(digit) for digit in num_str)
            return all(num_counter[digit] <= counter[digit] for digit in num_counter)

        result = [num for num in range(100, 1000, 2) if _filter(num)]
        return result


assert Solution().findEvenNumbers([2, 1, 3, 0]) == [
    102, 120, 130, 132, 210, 230, 302, 310, 312, 320
]

assert Solution().findEvenNumbers([2, 2, 8, 8, 2]) == [
    222, 228, 282, 288, 822, 828, 882
]

assert Solution().findEvenNumbers([3, 7, 5]) == []
