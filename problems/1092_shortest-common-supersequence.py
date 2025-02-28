# 1092. Shortest Common Supersequence
#
# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n_1, n_2 = len(str1), len(str2)
        dp = [[0 for _ in range(n_2 + 1)] for _ in range(n_1+1)]

        for i, row in enumerate(dp):
            row[0] = i

        for i, _ in enumerate(dp[0]):
            dp[0][i] = i

        for i in range(1, n_1 + 1):
            for j in range(1, n_2 + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        result = []
        i, j = n_1, n_2
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i, j = i-1, j-1
            elif dp[i-1][j] < dp[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1

        while i > 0:
            result.append(str1[i-1])
            i -= 1
        while j > 0:
            result.append(str2[j-1])
            j -= 1

        return "".join(reversed(result))


assert Solution().shortestCommonSupersequence("abac", "cab") == "cabac"

assert Solution().shortestCommonSupersequence(
    "aaaaaaaa",
    "aaaaaaaa"
) == "aaaaaaaa"
