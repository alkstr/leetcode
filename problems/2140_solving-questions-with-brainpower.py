# 2140. Solving Questions With Brainpower
#
# You are given a 0-indexed 2D integer array questions where questions[i] = [points_i, brainpower_i].
# The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you points_i points but you will be unable to solve each of the next brainpower_i questions. If you skip question i, you get to make the decision on the next question.
# - For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
#   - If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
#   - If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
# Return the maximum points you can earn for the exam.

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0 for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            points, skip = questions[i]
            dp[i] = dp[i+1]

            if i + skip + 1 <= N:
                dp[i] = max(dp[i], points + dp[i+skip+1])
            else:
                dp[i] = max(dp[i], points)

        return dp[0]


assert Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
assert Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
