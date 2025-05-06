# 771. Jewels and Stones
#
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

from typing import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(Counter(stones)[jewel] for jewel in jewels)


assert Solution().numJewelsInStones("aA", "aAAbbbb") == 3
assert Solution().numJewelsInStones("z", "ZZ") == 0
