# 407. Trapping Rain Water II
#
# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

from typing import List
import heapq


class Cell:
    def __init__(self, height: int, row: int, col: int):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.height < other.height


def is_cell_in_bounds(row: int, col: int, rows: int, cols: int):
    return 0 <= row < rows and 0 <= col < cols


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m = len(heightMap), len(heightMap[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        boundary_heapq = []
        result = 0

        for i in range(n):
            heapq.heappush(boundary_heapq, Cell(heightMap[i][0], i, 0))
            heapq.heappush(boundary_heapq, Cell(heightMap[i][m-1], i, m - 1))
            visited[i][0], visited[i][m-1] = True, True

        for i in range(m):
            heapq.heappush(boundary_heapq, Cell(heightMap[0][i], 0, i))
            heapq.heappush(boundary_heapq, Cell(heightMap[n-1][i], n - 1, i))
            visited[0][i], visited[n-1][i] = True, True

        while boundary_heapq:
            current_cell = heapq.heappop(boundary_heapq)
            for (i, j) in directions:
                neighbor_row, neighbor_col = current_cell.row + i, current_cell.col + j
                if (
                    is_cell_in_bounds(neighbor_row, neighbor_col, n, m)
                    and not visited[neighbor_row][neighbor_col]
                ):
                    neighbor_height = heightMap[neighbor_row][neighbor_col]
                    if neighbor_height < current_cell.height:
                        result += current_cell.height - neighbor_height

                    heapq.heappush(
                        boundary_heapq,
                        Cell(
                            max(neighbor_height, current_cell.height),
                            neighbor_row,
                            neighbor_col
                        )
                    )
                    visited[neighbor_row][neighbor_col] = True

        return result


assert Solution().trapRainWater(
    [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
) == 4

assert Solution().trapRainWater(
    [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3]
    ]
) == 10
