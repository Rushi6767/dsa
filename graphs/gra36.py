"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold edgesance
"""
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], edgesanceThreshold: int) -> int:
        dist = [[10**8 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != 10**8 and dist[via][j] != 10**8:
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        
        neighbour = n
        city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= edgesanceThreshold:
                    count+=1
            if count <= neighbour:
                neighbour = count
                city = i
        return city


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
edgesanceThreshold = 4
s = Solution()
print(s.findTheCity(n, edges, edgesanceThreshold))

"""
Time = Floyd-Warshall O(n³) + Edge Initialization O(E) + Neighbor Counting O(n²)
     = O(n³ + E + n²)
     ≈ O(n³)

Space = Distance Matrix O(n²) + Other Variables O(1)
      = O(n²)
"""