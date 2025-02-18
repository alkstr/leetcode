# 2375. Construct Smallest Number From DI String
#
# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
# A 0-indexed string num of length n + 1 is created using the following conditions:
# - num consists of the digits '1' to '9', where each digit is used at most once.
# - If pattern[i] == 'I', then num[i] < num[i + 1].
# - If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1
        used = [False for _ in range(10)]
        result = [-1 for _ in range(n)]

        def _backtrack(i: int) -> bool:
            if i == n:
                return True
            if result[i] == 0 or result[i] == 10:
                return False

            for num in range(1, 10):
                if used[num]:
                    continue
                if i != 0 and pattern[i-1] == "I" and result[i-1] > num:
                    continue
                if i != 0 and pattern[i-1] == "D" and result[i-1] < num:
                    return False

                used[num] = True
                result[i] = num
                if _backtrack(i + 1):
                    return True
                used[num] = False

            raise Exception("Unreachable")

        _backtrack(0)

        return "".join(str(i) for i in result)


assert Solution().smallestNumber("IIIDIDDD") == "123549876"
assert Solution().smallestNumber("DDD") == "4321"
