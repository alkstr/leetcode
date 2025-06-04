# 3403. Find the Lexicographically Largest String From the Box I
#
# You are given a string word, and an integer numFriends.
# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
# - word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# - All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        max_split_n = n - numFriends + 1

        result = word[:max_split_n]
        for left in range(n):
            result = max(
                result,
                word[left:min(n, left + max_split_n)]
            )

        return result


assert Solution().answerString("dbca", 2) == "dbc"
assert Solution().answerString("gggg", 4) == "g"
