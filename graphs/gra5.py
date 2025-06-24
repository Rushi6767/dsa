"""
Detect cycle in graph with bfs
"""

Vertex = 4
total_edges = 4
edges = [[0,1], [0,2], [1,2], [2,3]]

from collections import deque

class Solution:
    def isCycle(self, Vertex, edges):
        queue = deque()
        adj_list = [[] for _ in range(Vertex)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0] * Vertex

        for i in range(0, Vertex):
            if visited[i] == 1:
                continue

            queue.append((0,-1))
            visited[0] = 1

            while queue:
                node, parent = queue.popleft()

                for adjnode in adj_list[node]:
                    if visited[adjnode] == 0:
                        visited[adjnode] = 1
                        queue.append((adjnode, node))
                    
                    else:
                        if adjnode != parent:
                            return True
        return False

"""
Time complexity : O(n + 2e)
Space complexity : O(n) + O(n)
"""