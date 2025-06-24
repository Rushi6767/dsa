"""
detect cycle in graph with dfs
"""

Vertex = 4
total_edges = 4
edges = [[0,1], [0,2], [1,2], [2,3]]

from collections import deque

class Solution:
    def dfs(self, node, parents, visited, adj_list):
        visited[node] = 1
        for adj_node in adj_list:
            if visited[adj_node] == 0:
                ans = self.dfs(adj_node, node, visited, adj_list)
                if ans == True:
                    return True
            elif visited[adj_node] == 1 and adj_node != parents:
                return True
        return False


    def isCycle(self, Vertex, edges):
        adj_list = [[] for _ in range(Vertex)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0] * Vertex

        for i in range(0, Vertex):
            if visited[i] == 1:
                continue

            if self.dfs(i, -1, visited, adj_list) == True:
                return True
        return False

"""
Time complexity : O(V + 2E) == O(v + E)
Space complexity :(adj_list) O(v + E) + (visited) O(v) + recursion stack O(V) == O(v + E)
"""