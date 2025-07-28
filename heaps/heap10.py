"""
Kth largest element
"""
import heapq
from typing import List

class Solution:
    def better_findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        n = len(nums)

        # O(k log k)
        for i in range(k):
            heapq.heappush(ans, nums[i])

        # O((n-k) log k)
        for i in range(k, n):
            if nums[i] > ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans, nums[i])
        print(ans)
        return ans[0]



nums = [3,2,1,5,6,4]
k = 2
s = Solution()
print(s.better_findKthLargest(nums, k))

"""
Better
Time complexity: # # O(log k) + O((n-k) log k) == O(log k x (k + n - k)) == O(N log k)
Space complexity: O(k)
"""