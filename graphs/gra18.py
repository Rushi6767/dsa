"""
Detect Cycle in Directed Graph using kahn's algorithm
"""
from collections import deque

class Solution:
    def isCycle(self, V, edges):
        indegrees = [0 for _ in range(V)]
        adj_list = [[]for _ in range(V)]

        # O(n)
        for u,v in edges:
            adj_list[u].append(v)
            indegrees[v] += 1
        
        queue = deque()
        result = []

        # O(n)
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        # O(V + E)
        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for adj in adj_list[current_node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    queue.append(adj)

        if len(result) == V:
            return False
        return True
    
V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
s =Solution()
print(s.isCycle(V, edges))

"""
Time complexity :O(n) + O(n) + O(v + E)
Space complexity :O(n) + O(n) +O(n) == O(3n)
space : indegrees, adj_list, queue
"""