# 3085. Minimum Deletions to Make String K-Special
#
# You are given a string word and an integer k.
# We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.
# Here, freq(x) denotes the frequence of the character x in word, and |y| denotes the absolute value of y.
# Return the minimum number of characters you need to delete to make word k-special.

from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)

        result = len(word)
        for count_1 in counter.values():
            deletions = 0
            for count_2 in counter.values():
                if count_1 > count_2:
                    deletions += count_2
                elif count_2 > count_1 + k:
                    deletions += count_2 - (count_1 + k)

            result = min(result, deletions)

        return result


assert Solution().minimumDeletions("aabcaba", 0) == 3
assert Solution().minimumDeletions("dabdcbdcdcd", 2) == 2
assert Solution().minimumDeletions("aaabaaa", 2) == 1
