"""
Graph representation
"""
#1. store in matrix
n = 5
m = 6

edges = [[1,2], [2,4], [3,4], [1,3], [3,5], [5,4]]

matrix =[[0 for i in range(n + 1)] for i in range(n + 1)]

for u,v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1

# print(matrix)

# 2. store in List
lst = [[] for i in range(n+1)]
# print(lst)

for u,v in edges:
    lst[u].append(v)
    lst[v].append(u)

# print(lst)

# dictinary
d = {}
for i in range(1, n+1):
    d[i] = []

# print(d)
for u,v in edges:
    d[u].append(v)
    d[v].append(u)

print(d)