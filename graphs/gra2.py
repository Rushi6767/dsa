"""
DFS in graph
"""
class Solution:
    def dfs_algo(self, node, adj, visited, result):
        # 1. Visit this node
        result.append(node)
        visited[node] = 1

        # 2. Recurse on each unvisited neighbor
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs_algo(neighbor, adj, visited, result)

    def dfs(self, adj):
        total_nodes = len(adj)
        visited = [0] * total_nodes  # 0 = unvisited, 1 = visited
        result = []

        # Start DFS from node 0
        self.dfs_algo(0, adj, visited, result)
        return result
    
adj = [
    [1, 2],     # Neighbors of node 0
    [0, 3, 4],  # Neighbors of node 1
    [0, 4],     # Neighbors of node 2
    [1, 5],     # Neighbors of node 3
    [1, 2],     # Neighbors of node 4
    [3]         # Neighbors of node 5
]

sol = Solution()
print("DFS Traversal:", sol.dfs(adj))
    
"""
Time complexity: O(n) + O(2E)
Space complexity: O(2n) + O(n) which is stack space == O(n)
"""