# 2116. Check if a Parentheses String Can Be Valid
#
# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
# - It is ().
# - It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# - It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
# - If locked[i] is '1', you cannot change s[i].
# - But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        unlocked, opening = 0, 0
        for bracket, lock in zip(s, locked):
            if lock == "0":
                unlocked += 1
            elif bracket == "(":
                opening += 1
            elif bracket == ")" and opening > 0:
                opening -= 1
            elif bracket == ")" and unlocked > 0:
                unlocked -= 1
            else:
                return False

        balance = 0
        for bracket, lock in zip(reversed(s), reversed(locked)):
            if lock == "0":
                balance -= 1
                unlocked -= 1
            elif bracket == "(":
                balance += 1
                opening -= 1
            elif bracket == ")":
                balance -= 1
            if balance > 0:
                return False
            if unlocked == 0 and opening == 0:
                break

        if opening > 0:
            return False

        return True


assert Solution().canBeValid("))()))", "010100")
assert Solution().canBeValid("()()", "0000")
assert not Solution().canBeValid(")", "0")
