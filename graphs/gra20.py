"""
210. Course Schedule II
"""
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adj_list = [[]for _ in range(numCourses)]

        # O(n)
        for u,v in prerequisites:
            adj_list[v].append(u)
            indegrees[u] += 1
        
        queue = deque()
        result = []

        # O(n)
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        # O(V + E)
        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for adj in adj_list[current_node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    queue.append(adj)

        if len(result) == numCourses:
            return result
        return []


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# numCourses = 1
# prerequisites = []
s =  Solution()
print(s.findOrder(numCourses, prerequisites))

"""
Time complexity :O(n) + O(n) + O(v + E)
Space complexity :O(n) + O(n) +O(n) == O(3n)
space : indegrees, adj_list, queue
"""