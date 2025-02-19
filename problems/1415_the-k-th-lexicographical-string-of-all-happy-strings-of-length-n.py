# 1415. The k-th Lexicographical String of All Happy Strings of Length n
#
# A happy string is a string that:
# - consists only of letters of the set ['a', 'b', 'c'].
# - s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

from collections import deque


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        deq = deque()
        counter = 0
        result = ""

        def _backtrack(i: int):
            nonlocal counter, result

            if i == n:
                counter += 1
                if counter == k:
                    result = "".join(deq)
                return

            for c in "abc":
                if i == 0 or deq[-1] != c:
                    deq.append(c)
                    _backtrack(i + 1)
                    deq.pop()

        _backtrack(0)

        return result


assert Solution().getHappyString(1, 3) == "c"
assert Solution().getHappyString(1, 4) == ""
assert Solution().getHappyString(3, 9) == "cab"
