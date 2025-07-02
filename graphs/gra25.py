"""
Shortest path in Directed weight Acyclic Graph

1. topo sort on graph
2. take out the node and relax the edges
"""
from typing import List

class Solution:
    def dfs(self, current_node, stack, visited, adj_list):
        visited[current_node] = 1
        for adj, dist in adj_list[current_node]:
            if visited[adj] == 0:
                self.dfs(adj, stack, visited, adj_list)
        stack.append(current_node)


    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(V)]
        for i, j, k in edges:
            adj_list[i].append([j, k])
        
        stack = []
        visited = [0 for _ in range(V)]

        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, stack, visited, adj_list)
        
        distance = [float("inf") for _ in range(V)]
        distance[0] = 0

        # O(N + E)
        while len(stack) != 0:
            node = stack.pop()
            dist = distance[node]
            for adjNode, d in adj_list[node]:
                new_d = dist + d
                if new_d < distance[adjNode]:
                    distance[adjNode] = new_d

        # O(n)
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance


V = 6
E = 7
edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
s = Solution()
print(s.shortestPath(V, E, edges))


"""
Time complexity : O(E) [adj list] + O(V + E) [DFS] + O(V + E) [relaxation] + O(V) [replace inf]= O(V + E)
Space complexity : O(V + E)
"""