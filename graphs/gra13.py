"""
gfg : unique(distinct Island)
"""
class Solution:
    def dfs(self, r, c, base_r, base_c, shape, visited, rows, cols, grid):
        visited[r][c] = 1                      # mark current cell
        shape.append((r - base_r, c - base_c)) # store relative offset
        
        # four possible directions: up, left, down, right
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_i, new_j = r + x, y + c
            # skip if out of bounds
            if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                continue
            # skip water
            if grid[new_i][new_j] == 0:
                continue
            # skip already visited land
            if visited[new_i][new_j] == 1:
                continue
            # explore next land cell
            self.dfs(new_i, new_j, base_r, base_c, shape,
                     visited, rows, cols, grid)

    # main function
    def countDistinctIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        unique_islands = set()                 # will store unique shapes
        
        for r in range(rows):
            for c in range(cols):
                # start DFS only on unvisited land
                if grid[r][c] == 1 and visited[r][c] == 0:
                    shape = []                # list to hold current shape
                    self.dfs(r, c, r, c, shape, visited, rows, cols, grid)
                    unique_islands.add(tuple(shape))  # add shape to set
        return len(unique_islands)             # number of distinct shapes
    

grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]


sol = Solution()
print("Distinct Islands Count:", sol.countDistinctIslands(grid))
    
"""
Time complexity : O(r X c)
Space complexity : O(r X c)
"""

# ====bfs=====
from typing import List
from collections import deque

class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        unique_islands = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    shape = []
                    queue = deque()
                    queue.append((r, c))
                    visited[r][c] = 1
                    base_r, base_c = r, c
                    
                    while queue:
                        cur_r, cur_c = queue.popleft()
                        shape.append((cur_r - base_r, cur_c - base_c))
                        
                        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                            new_r, new_c = cur_r + dr, cur_c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols:
                                if grid[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                                    visited[new_r][new_c] = 1
                                    queue.append((new_r, new_c))
                                    
                    unique_islands.add(tuple(shape))
        
        return len(unique_islands)

# Test the BFS version with the sample input
grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

sol = Solution()
print("Distinct Islands Count (BFS):", sol.countDistinctIslands(grid))

"""
Time complexity : O(r X c)
Space complexity : O(r X c)
"""