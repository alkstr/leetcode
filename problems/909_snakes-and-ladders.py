# 909. Snakes and Ladders
#
# You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
# You start on square 1 of the board. In each move, starting from square curr, do the following:
# - Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
#   - This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# - If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# - The game ends when you reach the square n^2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.
# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.
# - For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n^2. If it is not possible to reach the square, return -1.

from collections import deque
from typing import List, Tuple


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)

        min_dist = [float("inf") for _ in range(N * N + 1)]
        min_dist[1] = 0

        def _pos(i: int) -> Tuple[int, int]:
            i, n = i - 1, N - 1

            x = n - i // N
            y = i % N if x % 2 == n % 2 else n - i % N
            return x, y

        deq = deque([1])
        while deq:
            current = deq.pop()
            for step in range(1, 7):
                if current + step > N * N:
                    continue

                x, y = _pos(current + step)
                next_cell = current + step \
                    if board[x][y] == -1 \
                    else board[x][y]

                if min_dist[current] + 1 >= min_dist[next_cell]:
                    continue

                min_dist[next_cell] = min_dist[current] + 1
                deq.append(next_cell)

        result = -1 if min_dist[-1] == float("inf") else min_dist[-1]
        return result


assert Solution().snakesAndLadders(
    [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
) == 4

assert Solution().snakesAndLadders([[-1, -1], [-1, 3]]) == 1
