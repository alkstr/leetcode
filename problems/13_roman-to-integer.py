# 13. Roman to Integer
#
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        N = len(s)
        CONVERSION = {
            "I": 1,    "IV": 4,   "V": 5,   "IX": 9,
            "X": 10,   "XL": 40,  "L": 50,  "XC": 90,
            "C": 100,  "CD": 400, "D": 500, "CM": 900,
            "M": 1000
        }

        result = 0
        i = 0
        while i < N:
            if i < N - 1 and s[i:i+2] in CONVERSION:
                result += CONVERSION[s[i:i+2]]
                i += 2
            else:
                result += CONVERSION[s[i]]
                i += 1

        return result


assert Solution().romanToInt("MDCCCLXXXIV") == 1884

assert Solution().romanToInt("III") == 3
assert Solution().romanToInt("LVIII") == 58
assert Solution().romanToInt("MCMXCIV") == 1994
