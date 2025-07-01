"""
802. Find Eventual Safe States using BFS
"""
from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vertex = len(graph)
        adj_list = [[] for _ in range(vertex)]
        indegrees = [0 for _ in range(vertex)]

        for node in range(vertex):
            for adj in graph[node]:
                adj_list[adj].append(node)
                indegrees[node] += 1

        queue = deque()

        # indegrees = [0 for _ in range(vertex)]
        # for node in range(vertex):
        #     for adj in adj_list[node]:
        #         indegrees[adj] += 1
        
        for node in range(vertex):
            if indegrees[node] == 0:
                queue.append(node)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for adj in adj_list[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    queue.append(adj)

        result.sort()
        return result




graph = [[1,2],[2,3],[5],[0],[5],[],[]]
s = Solution()
print(s.eventualSafeNodes(graph))

"""
Time complexity :O(n) + O(n) + O(v + E) + nlogn
Space complexity :O(n) + O(n) +O(n) == O(3n)
space : indegrees, adj_list, queue
"""