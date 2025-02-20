# 1980. Find Unique Binary String
#
# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = ["" for _ in range(n)]
        nums_set = set(nums)

        def _backtrack(i: int) -> bool:
            if i == n:
                return "".join(result) not in nums_set

            result[i] = "0"
            if _backtrack(i + 1):
                return True

            result[i] = "1"
            if _backtrack(i + 1):
                return True

            return False

        if not _backtrack(0):
            raise Exception("Unreachable")

        result = "".join(result)
        return result


assert Solution().findDifferentBinaryString(["01", "10"]) in ("00", "11")
assert Solution().findDifferentBinaryString(["00", "01"]) in ("10", "11")

assert Solution().findDifferentBinaryString(
    ["111", "011", "001"]
) in ("000", "010", "100", "101", "110")
