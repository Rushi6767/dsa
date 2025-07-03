"""
1631. Path With Minimum Effort
"""
from typing import List
import sys
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        visited = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        visited[0][0] = 0
        p_queue = [[0,0,0]]

        while p_queue:
            dist, i, j = heapq.heappop(p_queue)

            if i == rows-1 and j == cols-1:
                return dist
            
            for x, y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                    continue
                effort =max(dist,  abs(heights[new_i][new_j] - heights[i][j]))
                if effort < visited[new_i][new_j]:
                    visited[new_i][new_j] = effort
                    heapq.heappush(p_queue, [effort, new_i, new_j])

        return visited[rows-1][cols-1]

heights = [[1,2,2],[3,8,2],[5,3,5]]
s = Solution()
print(s.minimumEffortPath(heights))

"""
Time complexity : O(E logV) == O(nxmx4 log(nxm))
Space complexity :O(m * n)
"""