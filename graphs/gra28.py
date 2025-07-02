"""
Print the shortest path in weight undirected graph
"""

import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        parent = [i for i in range(V + 1)]
        dist_to_src = float("inf")
        adj_list = [[] for _ in range(V+1)]
        for i, j, k in edges:
            adj_list[i].append([j, k])
            adj_list[j].append([i, k])
        
        distance = [float("inf") for _ in range(V+1)]
        distance[src] = 0

        priority_queue = [[0, src]]
        
        # O(E logV)
        while priority_queue:
            curr_distance, node = heapq.heappop(priority_queue)
            print(curr_distance, node)
            if curr_distance > distance[node]:
                continue

            for adj_node, weight in adj_list[node]:
                travel = curr_distance + weight
                if travel < distance[adj_node] :
                    distance[adj_node] = travel
                    heapq.heappush(priority_queue, [travel, adj_node])
                    parent[adj_node] = node

        if distance[V] == float("inf"):
            return [-1]
        
        node = V
        path = []

        # O(V)
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        # O(V)
        path.reverse()
        return path

n = 5
edges = [
  [1,2,2], [2,5,5],
  [2,3,4], [1,4,1],
  [4,3,3], [3,5,1]
]
s = Solution()
print(s.dijkstra(n, edges, 1))


"""
Time complexity : O(E logV) + O(V) + O(V)

Space complexity :O(V + E) + )(V)
"""
       