"""
787. Cheapest Flights Within K Stops
"""
from collections import deque
from typing import List
import sys

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for i, j, ka in flights:
            adj_list[i].append([j, ka])
        
        distance = [sys.maxsize for _ in range(n)]
        distance[src] = 0

        queue = deque()
        queue.append([0,src,0])

        while queue:
            stop, node, cost = queue.popleft()

            # if cost > distance[node]:
            #     continue

            for adj_node, price in adj_list[node]:
                new_cost = cost + price
                if new_cost < distance[adj_node] :
                    new_stop = stop + 1
                    if new_stop ==  k + 1:
                        if adj_node != dst:
                            continue

                    distance[adj_node] = new_cost
                    queue.append([new_stop, adj_node, new_cost])

        if distance[dst] == sys.maxsize:
            return -1
        return distance[dst]

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
s = Solution()
print(s.findCheapestPrice(n, flights, src, dst, k))

"""
Time complexity : len(flights)
Space complexity :O(V + E)
"""