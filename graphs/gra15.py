"""
Topological sort using DFS
"""

class Solution:
    def dfs(self, current_node, visited, stack, adj_list):
        visited[current_node] = 1
        for adj in adj_list[current_node]:
            if visited[adj] == 0:
                self.dfs(adj, visited, stack, adj_list)
        stack.append(current_node)

    def toposort(self, Vertext, edges):
        adj_list = [[] for _ in range(Vertext)]
        for u,v in edges:
            adj_list[u].append(v)
        stack = []
        visited = [0 for _ in range(Vertext)]

        for i in range(Vertext):
            if visited[i] == 0:
                self.dfs(i,  visited, stack, adj_list)

        return stack[::-1]

Vertext = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]
s = Solution()
print(s.toposort(Vertext, edges))

"""
Time complexity : O(V + E)
Space complexity : O(V + E)
"""