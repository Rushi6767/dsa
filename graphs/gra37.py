"""
Minimum Spaning Tree
Minimum sum of spaning trees
Spaning Tree : A tree with n node and n-1 edges and all the nodes should be reachable
"""

from typing import List
import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        mst = []
        total = 0
        visited = [0 for _ in range(V)]
        priority_queue = [[0,0,-1]]

        # O(E)
        while priority_queue:
            # O(log(E))
            weight, node, parent = heapq.heappop(priority_queue)
            if visited[node] == 0:
                visited[node] = 1
                if parent != -1:
                    total += weight
                    mst.append([parent, node]) 
                # O(E)
                for adj_node, wtt in adj[node]:
                    if visited[adj_node] == 0:
                        # O(log(E))
                        heapq.heappush(priority_queue, [wtt, adj_node, node])
        return total

V = 3
edges = [
    [0, 1, 5],
    [1, 2, 3],
    [0, 2, 1]
]
adj = [[] for _ in range(V)]
for u, v, w in edges:
    adj[u].append([v, w])
    adj[v].append([u, w])
s = Solution()
print(s.spanningTree(V, adj))

"""
Time complexity : # O(2(E log(E))
Space complexity : O(V + E)   # If you ignore mst
O(V + E + V) = O(V + E)  # Even if mst is included
"""