"""
Dijkstra Algorithm with set(best in java, c++)
Worst time complexity
we can also use queue
but, Worst time complexity
"""
import sys

class Solution:
    def dijkstra(self, V, edges, src):
        adj_list = [[] for _ in range(V)]
        for i,j,k in edges:
            adj_list[i].append([j,k])

        distance = [sys.maxsize for _ in range(V)]
        distance[src] = 0

        my_set = set()
        my_set.add((0,src))

        while my_set: # O(V)
            dist,node = min(my_set)  #O(V)
            my_set.discard((dist, node))
            for adjNode, weight in adj_list[node]:
                dist_trav = dist + weight
                if dist_trav < distance[adjNode]:
                    if distance[adjNode] != sys.maxsize:
                        my_set.discard((distance[adjNode], adjNode))
                    distance[adjNode] = dist_trav
                    my_set.add((dist_trav, adjNode))
        return distance



V = 5
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0
s = Solution()
print(s.dijkstra(V, edges, src))