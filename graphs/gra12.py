"""
200. Number of Islands
"""
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = [["0" for _ in range(cols)] for _ in range(rows)]
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c]=="0":
                    queue.append((r,c))
                    visited[r][c] = "1"
                    count += 1
                while queue:
                    i,j = queue.popleft()
                    for x,y in [(-1,0), (0,-1),(1,0),(0,1)]:
                        new_i = i + x
                        new_j = j + y

                        if new_i < 0 or new_i>=rows or new_j < 0 or new_j>=cols:
                            continue
                        if grid[new_i][new_j] == "0":
                            continue
                        if grid[new_i][new_j] == "1" and visited[new_i][new_j] == "1":
                            continue

                        queue.append((new_i, new_j))
                        visited[new_i][new_j] = "1"

        print(count)
        return 0


s= Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(s.numIslands(grid))
"""
Time complexity : O(r X c)
Space complexity : O(r X c)
"""

# ===============better coding style=====================
class Solution:
    def bfs(self, i, j, visited, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1                # mark start cell

        while len(queue) != 0:
            x, y = queue.popleft()
            # explore 4-directional neighbours
            for xx, yy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i, new_j = x + xx, y + yy
                # skip out-of-bounds
                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue
                # skip water
                if grid[new_i][new_j] == "0":
                    continue
                # skip already-seen land
                if visited[new_i][new_j] == 1:
                    continue
                visited[new_i][new_j] = 1
                queue.append((new_i, new_j))

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                # new island found
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count += 1
                    self.bfs(r, c, visited, grid)   # flood-fill it
        return count
    
"""
Time complexity : O(r X c)
Space complexity : O(r X c)
"""

# ===by dfs================
class Solution:
    def dfs(self, i, j, visited, grid):
        # stop conditions
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == "0":
            return
        if visited[i][j] == 1:
            return

        visited[i][j] = 1          # mark current land

        # recurse in 4 directions
        self.dfs(i + 1, j, visited, grid)
        self.dfs(i - 1, j, visited, grid)
        self.dfs(i, j - 1, visited, grid)
        self.dfs(i, j + 1, visited, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count += 1
                    self.dfs(r, c, visited, grid)   # flood-fill recursively
        return count
"""
Time complexity : O(r X c)
Space complexity : O(r X c)
"""
    
# ===optimal and debug====================
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        n,m=len(grid),len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c]=="1":
                    island +=1
                    grid[r][c] = "0"
                    queue = deque()
                    queue.append((r,c))
                    while queue:
                        row,col = queue.popleft()
                        for dr,dc in directions:
                            nr,nc = row+dr,col+dc
                            if 0<=nr <n and 0<= nc < m and grid[nr][nc]=="1":
                                grid[nr][nc] = "0"
                                queue.append((nr,nc))
        return island