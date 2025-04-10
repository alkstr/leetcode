# 2999. Count the Number of Powerful Integers
#
# You are given three integers start, finish, and limit. You are also given a 0-indexed string s representing a positive integer.
# A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.
# Return the total number of powerful integers in the range [start..finish].
# A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def calc(finish, suffix: str, limit: int) -> int:
            N_f, N_s = len(finish), len(suffix)
            if int(finish) < int(suffix):
                return 0
            if N_f == N_s:
                return 1

            finish_suffix = finish[N_f-N_s:]
            count = 0
            iterations = N_f - N_s

            for i in range(iterations):
                if limit < int(finish[i]):
                    count += (limit + 1) ** (iterations - i)
                    return count
                count += int(finish[i]) * (limit + 1) ** (iterations - 1 - i)

            if finish_suffix >= suffix:
                count += 1

            return count

        start_str = str(start - 1)
        finish_str = str(finish)
        return calc(finish_str, s, limit) - calc(start_str, s, limit)


assert Solution().numberOfPowerfulInt(20, 1159, 5, "20") == 8

assert Solution().numberOfPowerfulInt(1, 6000, 4, "124") == 5
assert Solution().numberOfPowerfulInt(15, 215, 6, "10") == 2
assert Solution().numberOfPowerfulInt(1000, 2000, 4, "3000") == 0
