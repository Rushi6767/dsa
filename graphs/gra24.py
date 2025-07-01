"""
Shortest Path in Undirected Graph
"""

from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        vertex = len(adj)
        distance_list = [-1 for _ in range(vertex)]
        queue = deque()
        queue.append([src, 0])
        distance_list[src] = 0

        while queue:
            node, distance = queue.popleft()
            for i in adj[node]:
                if distance_list[i] == -1:
                    distance_list[i] = distance + 1
                    queue.append([i, distance+1])


        return distance_list


adj = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src=0
s = Solution()
print(s.shortestPath(adj, src))

"""
Time complexity :O(v + E)
Space complexity :O(n)
"""