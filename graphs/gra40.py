"""
Number of Provinces
"""

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
            return
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return

class Solution:
    def numProvinces(self, adj, V):
        ds = DisJointSet(V)

        # TC : O(V^2 X 4 X alpha)
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    ds.union_by_rank(i, j)

        count = 0
        # TC : O(V X 4 X alpha)
        for i in range(V):
            if ds.find(i) == i:
                count += 1
        return count

v = 3
adj = [[1, 0, 1],[0, 1, 0],[1, 0, 1]]
s = Solution()
print(s.numProvinces(adj, v))



"""
Time complexity : O(V^2 X 4 X alpha) + O(V X 4 X alpha)
Space complexity : parent O(n) + rank O(n) = O(n)
"""