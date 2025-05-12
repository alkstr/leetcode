# 12. Integer to Roman
#
# Given an integer, convert it to a Roman numeral.

class Solution:
    def intToRoman(self, num: int) -> str:
        CONVERSION = [
            (1000, "M"),
            (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"),  (50, "L"),  (40, "XL"),  (10, "X"),
            (9, "IX"),   (5, "V"),   (4, "IV"),   (1, "I")
        ]

        i = 0
        result = ""
        while num:
            arabic, roman = CONVERSION[i]

            if num < arabic:
                i += 1
            else:
                result += roman
                num -= arabic

        return result


assert Solution().intToRoman(3749) == "MMMDCCXLIX"
assert Solution().intToRoman(58) == "LVIII"
assert Solution().intToRoman(1994) == "MCMXCIV"
