"""
1020. Number of Enclaves
"""
# from typing import List

# class Solution:
#     def dfs(self, r,c,visited,rows,cols, grid):
#         if r<0 or r>=rows or c<0 or c>=cols:
#             return
#         if grid[r][c] == 0:
#             return
#         if visited[r][c] == 1:
#             return

#         visited[r][c] = 1
#         self.dfs(r-1,c,visited,rows,cols, grid)
#         self.dfs(r,c-1,visited,rows,cols, grid)
#         self.dfs(r,c+1,visited,rows,cols, grid)
#         self.dfs(r+1,c,visited,rows,cols, grid)

#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         """
#         Do not return anything, modify grid in-place instead.
#         """
#         count = 0
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = [[0 for _ in range(cols)] for _ in range(rows)]

#         for r in range(rows):
#             for c in range(cols):
#                 if r==0 or c==0 or r==rows-1 or c==cols-1:
#                     if grid[r][c] == 1:
#                         if visited[r][c] == 0:
#                             self.dfs(r,c,visited,rows,cols,grid)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]==1 and visited[r][c] == 0:
#                     grid[r][c] = 0
#                     count += 1
#         return count
    

# grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

# s = Solution()
# print(s.numEnclaves(grid))

# for row in grid:
#     print(row)

from collections import deque

class Solution:
    def numEnclaves(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if grid[r][c] == 1:
                        queue.append((r,c))
                        visited[r][c] = 1
        while queue:
            i,j = queue.popleft()
            for x,y in [(-1,0), (0,-1),(1,0),(0,1)]:
                new_i = i + x
                new_j = j + y

                if new_i < 0 or new_i>=rows or new_j < 0 or new_j>=cols:
                    continue
                if grid[new_i][new_j] == 0:
                    continue
                if grid[new_i][new_j] == 1 and visited[new_i][new_j] == 1:
                    continue

                queue.append((new_i, new_j))
                visited[new_i][new_j] = 1

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c]==0:
                    count += 1
        return count


s= Solution()
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(s.numEnclaves(grid))
"""
Time complexity : O(r X c)
Space complexity : O(r X c)
"""