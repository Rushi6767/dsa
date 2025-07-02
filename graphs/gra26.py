"""
Dijkstra Algorithm with priority queue (best in python)

it is not work
1. single -ve weight
2. -ve cycle
"""
import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        adj_list = [[] for _ in range(V)]
        for i, j, k in edges:
            adj_list[i].append([j, k])
        
        distance = [float("inf") for _ in range(V)]
        distance[src] = 0

        priority_queue = [[0, src]]

        while priority_queue:
            curr_distance, node = heapq.heappop(priority_queue)
            if curr_distance > distance[node]:
                continue

            for adj_node, weight in adj_list[node]:
                travel = curr_distance + weight
                if travel < distance[adj_node] :
                    distance[adj_node] = travel
                    priority_queue.append([travel, adj_node])

        return distance

V = 5
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0
s = Solution()
print(s.dijkstra(V, edges, src))

"""
Total Edges : E
priority queue : logV

Time complexity :ElogV

adj_list:     O(V + E)
distance:     O(V)
priority queue: O(V) ~ O(E)
Space complexity :O(V + E)
"""
        