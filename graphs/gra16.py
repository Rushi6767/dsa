"""
Cycle detection in directed graph by dfs
"""

class Solution:
    def dfs(self, node, visited, path_visited, adj_list):
        visited[node] = 1
        path_visited[node] = 1
        for adj_node in adj_list[node]:
            if visited[adj_node] == 0:
                ans = self.dfs(adj_node, visited, path_visited, adj_list)

                if ans == True:
                    return True
            elif path_visited[adj_node] == 1:
                return True
        path_visited[node] = 0
        return False


    def isCycle(self, Vertex, edges):
        adj_list = [[] for _ in range(Vertex)]

        for u,v in edges:
            adj_list[u].append(v)

        visited = [0] * Vertex
        path_visited = [0] * Vertex

        for i in range(0, Vertex):
            if visited[i] == 0:
                ans = self.dfs(i, visited, path_visited, adj_list)
                if ans == True:
                    return True
        return False

Vertex = 4
# edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
s = Solution()
print(s.isCycle(Vertex, edges))

"""
Time complexity :O(v + E)
Space complexity :O(n)
"""