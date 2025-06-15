# 1432. Max Difference You Can Get From Changing an Integer
#
# You are given an integer num. You will apply the following steps to num two separate times:
# - Pick a digit x (0 <= x <= 9).
# - Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# - Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
# Return the max difference between a and b.
# Note that neither a nor b may have any leading zeros, and must not be 0.

class Solution:
    def maxDiff(self, num: int) -> int:
        max_value = min_value = str(num)

        for digit in max_value:
            if digit != "9":
                max_value = max_value.replace(digit, "9")
                break

        if min_value[0] == "1":
            for digit in min_value:
                if digit not in "01":
                    min_value = min_value.replace(digit, "0")
                    break
        else:
            min_value = min_value.replace(min_value[0], "1")

        result = int(max_value) - int(min_value)
        return result


assert Solution().maxDiff(555) == 888
assert Solution().maxDiff(9) == 8
