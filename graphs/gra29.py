"""
1091. Shortest Path in Binary Matrix
"""
from typing import List
from collections import deque
import sys

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        distance =[[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 1

        queue = deque()
        queue.append([1, 0, 0])

        while queue:
            dist, i, j = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
                new_i, new_j = i + dx, j + dy
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                    continue

                if grid[new_i][new_j] == 1:
                    continue

                dis_tra = dist + 1

                if dis_tra < distance[new_i][new_j]:
                    distance[new_i][new_j] = dis_tra
                    queue.append([dis_tra, new_i, new_j])

        if distance[rows-1][cols-1] == sys.maxsize:
            return -1
        return distance[rows-1][cols-1]



grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[0,1],[1,0]]
s = Solution()
print(s.shortestPathBinaryMatrix(grid))