"""
1319. Number of Operations to Make Network Connected
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisJointSet(n)
        extra_edges = 0
        connected_componant = 0

        # TC : O(E 4 alpha)

        for i in connections:
            u, v = i
            ds.union_by_rank(u, v)
            if ds.find(u) == ds.find(v) and ds.find(u) != u and ds.find(v) != v:
                extra_edges +=1

        # TC : O(v)
        for h in range(n):
            if ds.find(h) == h:
                connected_componant += 1

        ans = connected_componant -1

        if extra_edges >= ans:
            return ans
        
        return -1


n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]

s = Solution()
print(s.makeConnected(n, connections))

"""
Time complexity :O(n * α(n)) + O(E * α(n)) ≈ ≈ O(n) + O(E) = O(n + E)
Space complexity : parent O(n) + rank O(n) = O(n)
"""


# from typing import List

# class DisJointSet:
#     def __init__(self, n):
#         self.parent = [i for i in range(n+1)]
#         self.rank = [0] * (n+1)

#     def find(self, x):
#         if x == self.parent[x]:
#             return x
        
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union_by_rank(self, u, v):
#         pu = self.find(u)
#         pv = self.find(v)

#         if pu == pv:
#             return True
        
#         if self.rank[pu] < self.rank[pv]:
#             self.parent[pu] = pv

#         elif self.rank[pu] > self.rank[pv]:
#             self.parent[pv] = pu

#         else:
#             self.parent[pv] = pu
#             self.rank[pu] += 1
#         return False

# class Solution:
#     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         ds = DisJointSet(n)
#         extra_edges = 0
#         connected_componant = 0

#         for u,v in connections:
#             if ds.union_by_rank(u, v) :
#                 extra_edges +=1

#         for h in range(n):
#             if ds.find(h) == h:
#                 connected_componant += 1
        
#         if extra_edges>= connected_componant -1:
#             return connected_componant -1        
#         return -1
        