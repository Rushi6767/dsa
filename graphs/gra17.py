"""
Topological sort using kahn's algorithm (bfs)
"""
from collections import deque

class Solution:
    
    def topoSort(self, Vertex, edges):
        indegrees = [0 for _ in range(Vertex)]
        adj_list = [[]for _ in range(Vertex)]

        # O(n)
        for u,v in edges:
            adj_list[u].append(v)
            indegrees[v] += 1
        
        queue = deque()
        result = []

        # O(n)
        for i in range(Vertex):
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

        return result

Vertex = 4
total_edge = 3
edges= [[3, 0], [1, 0], [2, 0]]
s = Solution()
print(s.topoSort(Vertex, edges))


"""
Time complexity :O(n) + O(n) + O(v + E)
Space complexity :O(n) + O(n) +O(n) == O(3n)
space : indegrees, adj_list, queue
"""