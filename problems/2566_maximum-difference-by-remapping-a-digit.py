# 2566. Maximum Difference by Remapping a Digit
#
# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
# Notes:
# - When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
# - Bob can remap a digit to itself, in which case num does not change.
# - Bob can remap different digits for obtaining minimum and maximum values respectively.
# - The resulting number after remapping can contain leading zeroes.


class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        def _replace_first(to: str) -> str:
            if num_str.count(to) == len(num_str):
                return num_str

            for digit in num_str:
                if digit != to:
                    return num_str.replace(digit, to)

        max_value = int(_replace_first("9"))
        min_value = int(_replace_first("0"))

        result = max_value - min_value
        return result


assert Solution().minMaxDifference(11891) == 99009
assert Solution().minMaxDifference(90) == 99
