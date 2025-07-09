"""
DisJoint Set

Dynamic Graph

Finding Parent()
Union()
Rank, Size

union(u,v) by rank
1. Find ultimate parent (pu, pv) of u and v
2. Find rank of pu and pv
3. Connect small rank to large rank

path compression
"""

class DisJointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)

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

    def union_by_size(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

        elif self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

ds = DisJointSet(7)
# ds.union_by_rank(1,2)
# ds.union_by_rank(2,3)
# ds.union_by_rank(4,5)
# ds.union_by_rank(6,7)
# ds.union_by_rank(5,6)
# ds.union_by_rank(3,7)


ds.union_by_size(1,2)
ds.union_by_size(2,3)
ds.union_by_size(4,5)
ds.union_by_size(6,7)
ds.union_by_size(5,6)
ds.union_by_size(3,7)

print(ds.find(1))
print(ds.find(7))
print(ds.size)

"""
Time complexity : O(α(n))
Space complexity : O(n)
"""