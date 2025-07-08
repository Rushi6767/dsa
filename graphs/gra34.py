"""
Bellman-Ford Algorithm (Detect Negative cycle)
1. Relax all the edges n-1 times
2. if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
"""
class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8 for _ in range(V)]
        dist[src] = 0
        
        for _ in range(V-1):
            for u,v,w in edges:
                if dist[u] != 10**8:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        
        for u,v,w in edges:
            if dist[u] != 10**8:
                if dist[u] + w < dist[v]:
                    return [-1]
        
        return dist
    
V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
s = Solution()
print(s.bellmanFord(V, edges, src))
                    
"""
Time complexity: O(V * E)
Space complexity: O(V)
"""