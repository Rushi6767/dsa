"""
Minimum Multiplications to reach End
"""

from typing import List
from collections import deque
import sys
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        distance = [sys.maxsize for _ in range(100000)]
        distance[start] = 0

        queue = deque()
        queue.append([0, start])

        while queue:
            step, num = queue.popleft()
            if num == end:
                return step
            for m in arr:
                new_num = (num * m) % 100000
                new_step = step + 1
                if new_step< distance[new_num]:
                    distance[new_num] = new_step
                    queue.append([new_step, new_num])

        return -1



arr = [2, 5, 7]
start = 3
end = 30
s = Solution()
print(s.minimumMultiplications(arr,start, end))