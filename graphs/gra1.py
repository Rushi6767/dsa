"""
BFS in Graph
"""

from collections import deque

class Solution:
    # Function that does BFS from 'start' and returns the visit order.
    def bfs_algo(self, n, adj, start):
        ans = []                  # stores the BFS order
        visited = [0] * n         # 0 = unvisited, 1 = visited
        queue = deque([start])    # our queue, seeded with the start node
        visited[start] = 1

        while queue:
            u = queue.popleft()   # take the next node
            ans.append(u)         # record it

            # enqueue all unvisited neighbors
            for v in adj[u]:
                if visited[v] == 0:
                    visited[v] = 1
                    queue.append(v)

        return ans
 
    def bfs(self, adj):
        n = len(adj)
        return self.bfs_algo(n, adj, 0)
    

adj = [
    [1, 2],     # Neighbors of node 0
    [0, 3, 4],  # Neighbors of node 1
    [0, 4],     # Neighbors of node 2
    [1, 5],     # Neighbors of node 3
    [1, 2],     # Neighbors of node 4
    [3]         # Neighbors of node 5
]

sol = Solution()
print("BFS Traversal:", sol.bfs(adj))
    
"""
Time complexity: O(n) + O(2E)
Space complexity: O(3n) == O(n)
"""