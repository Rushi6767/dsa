"""
802. Find Eventual Safe States using DFS
"""

from typing import List

class Solution:
    def dfs(self, current_node, adj_list, visited, path_visited, safe):
        visited[current_node] = 1
        path_visited[current_node] = 1

        for adj in adj_list[current_node]:
            if visited[adj] == 0:
                ans = self.dfs(adj,adj_list, visited, path_visited, safe)
                if ans == False:
                    return False
            elif path_visited[adj] == 1:
                return False
        safe[current_node] = 1
        path_visited[current_node] = 0
        return True
        

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vertex = len(graph)
        visited = [0 for _ in range(vertex)]
        path_visited = [0 for _ in range(vertex)]
        safe = [0 for _ in range(vertex)]

        for i in range(vertex):
            if visited[i] == 0:
                self.dfs(i,graph, visited, path_visited, safe)

        result = []
        for i in range(vertex):
            if safe[i] == 1:
                result.append(i)

        return result

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
s = Solution()
print(s.eventualSafeNodes(graph))

"""
O(V)+O(V)+O(V)+O(V)=O(4V)=O(V)
visited, path_visited, safe, stack space

Time complexity :O(v + E)
Space complexity :O(n)
"""