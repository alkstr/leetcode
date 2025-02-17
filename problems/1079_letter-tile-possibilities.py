# 1079. Letter Tile Possibilities
#
# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_to_freq = Counter(tiles)
        count_ref = [0]

        def _backtrack():
            for char, freq in char_to_freq.items():
                if freq == 0:
                    continue

                char_to_freq[char] -= 1
                count_ref[0] += 1
                _backtrack()
                char_to_freq[char] += 1

        _backtrack()

        return count_ref[0]


assert Solution().numTilePossibilities("AAB") == 8
assert Solution().numTilePossibilities("AAABBC") == 188
assert Solution().numTilePossibilities("V") == 1
