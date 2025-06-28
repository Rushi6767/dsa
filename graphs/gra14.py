"""
785. Is Graph Bipartite?
"""
from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = deque()
        n = len(graph)
        visited = [0] * n

        for i in range(0, n):
            if visited[i] == 1:
                continue

            queue.append((0,-1))
            visited[0] = 1
            edges = 0

            while queue:
                node, parent = queue.popleft()

                for adjnode in graph[node]:
                    edges += 1
                    if visited[adjnode] == 0:
                        visited[adjnode] = 1
                        queue.append((adjnode, node))
                    
                    else:
                        if adjnode != parent:
                            cycle =  True
        ed = edges//2
        if cycle:
            if ed%2 == 0:
                return True
            return False


s = Solution()
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
print(s.isBipartite(graph))
