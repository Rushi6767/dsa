"""
703. Kth Largest Element in a Stream
"""
from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        # Build min-heap of size k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

k = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(k.add(10))  # Should return 8
print(k.add(2))   # Should return 7
print(k.add(9))   # Should return 8


"""
__init_
Time complexity: O(n log k)
Space complexity: O(k)

add(val)
Time complexity: O(log k)
Space complexity: O(k)
"""