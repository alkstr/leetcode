# 9. Palindrome Number
#
# Given an integer x, return true if x is a palindrome, and false otherwise.

def get_digit(number: int, n: int) -> int:
    return (number // 10 ** n) % 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        left, right = 0, 10

        while x // (10 ** right) == 0:
            right -= 1

        while left < right:
            if get_digit(x, right) != get_digit(x, left):
                return False
            left, right = left + 1, right - 1

        return True


assert Solution().isPalindrome(121)
assert not Solution().isPalindrome(-121)
assert not Solution().isPalindrome(-10)

assert Solution().isPalindrome(0)
