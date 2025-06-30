"""
785. Is Graph Bipartite?
"""
from typing import List

class Solution:
    def dfs(self, current_node, visited, graph, color):
        visited[current_node] = color
        for adj_node in graph[current_node]:
            if visited[adj_node] != -1:
                if visited[adj_node] == color:
                    return False
            else:
                # ans = self.dfs(adj_node,visited, graph, 1-color)  better approach
                if color == 0:
                    ans = self.dfs(adj_node,visited, graph, 1)
                else :
                    ans = self.dfs(adj_node,visited, graph, 0)
                if ans == False:
                    return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1] * n
        for i in range(n):
            if visited[i] == -1:
                ans = self.dfs(i, visited, graph, 0)
                if ans == False:
                    return False
        return True



s = Solution()
# graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
print(s.isBipartite(graph))


"""
Time complexity : O(n + 2e) == O(n + e)
Space complexity : O(n)
"""