# 386. Lexicographical Numbers
#
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def _dfs(current: int):
            if current > n:
                return

            result.append(current)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    break
                _dfs(next_num)

        for i in range(1, 10):
            _dfs(i)

        return result


assert Solution().lexicalOrder(13) == [
    1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
]

assert Solution().lexicalOrder(2) == [1, 2]
