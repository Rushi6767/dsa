"""
Minimum Spanning Tree Using Kruskal’s Algorithm
"""

from typing import List

class DisJointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_rank(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True
    
class Solution:
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        edges = []
        seen = set()

        # Tc : O(V + E)
        for u in range(V):
            for neighbour in adj[u]:
                v, w = neighbour
                if (min(v, u), max(v,u)) not in seen:
                    seen.add((min(v, u), max(v,u)))
                    edges.append((w, u, v))

        # Tc : O(M logM)
        edges.sort()

        djs = DisJointSet(V)
        mst_weight = 0

        # Tc : O(M X 4 X alpha)
        for w,u,v in edges:
            if djs.union_by_rank(u,v):
                mst_weight += w
        return mst_weight
    

V = 3

edges = [
    [0, 1, 5],
    [1, 2, 3],
    [0, 2, 1]
]

adj = [[] for _ in range(V)]

for u, v, w in edges:
    adj[u].append([v, w])
    adj[v].append([u, w])  # undirected graph

s = Solution()
print(s.spanningTree(V, adj))


"""
Time complexity : O(V + E) + O(M logM) + O(M X 4 X alpha)
Space complexity : parent O(V) + rank O(V) + Edge O(E) + seen set O(E) == O(V + E)
"""