# 1399. Count Largest Group
#
# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.

from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = Counter()

        for i in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            counter[digit_sum] += 1

        max_count = max(counter.values())
        result = sum(count == max_count for count in counter.values())
        return result


assert Solution().countLargestGroup(13) == 4
assert Solution().countLargestGroup(2) == 2
