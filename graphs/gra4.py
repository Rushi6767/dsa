"""
733. Flood Fill
"""

from copy import deepcopy
from typing import List


class Solution:
    def dfs(self, i, j, new_color, initial_color, visited, rows, cols):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if visited[i][j] != initial_color:
            return
        if visited[i][j] == initial_color:
            visited[i][j] = new_color
            
        self.dfs(i + 1, j, new_color, initial_color, visited, rows, cols)
        self.dfs(i, j + 1, new_color, initial_color, visited, rows, cols)
        self.dfs(i - 1, j, new_color, initial_color, visited, rows, cols)
        self.dfs(i, j - 1, new_color, initial_color, visited, rows, cols)

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
            
        visited = deepcopy(image)
        rows = len(visited)
        cols = len(visited[0])
        initial_color = visited[sr][sc]
        
        self.dfs(sr, sc, color, initial_color, visited, rows, cols)
        
        return visited
    
"""
Time complexity : O(R x C X 4)
Space complexity : O(R x C) + O(R X C) == visited arry + stack space
"""
# ========bfs============
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]]) -> int:
        rows = len(image)
        cols = len(image[0])
        image_copy = deepcopy(image)
        sr = 1
        sc = 0
        color = 2
        init_color = image_copy[sr][sc]

        if image_copy[sr][sc] == color:
            return image_copy

        queue = deque()
        queue.append((sr, sc))
        
        while len(queue) != 0 :
            i, j = queue.popleft()
            image_copy[i][j] = color
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + dx, j + dy
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                    continue
                if image_copy[new_i][new_j] != init_color:
                    continue
           
                queue.append((new_i, new_j))                 
        return image_copy
    
image = [[0,0,0],[0,0,0]]

sol = Solution()
result = sol.floodFill(image)
print("final image:", result)
    
"""
Time complexity : O(R x C X 4)
Space complexity : O(R x C) + O(R X C) == visited arry + stack space
"""