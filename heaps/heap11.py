"""
Find Kth largest element using Quick select and partition Algorithm
"""
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        while True:
            pivot_index = self.randomIndex(left, right)
            pivot_index = self.partitionAndReturnIndex(nums, pivot_index, left, right)
            if pivot_index == k-1:
                return nums[pivot_index]
            elif pivot_index > k-1:
                right = pivot_index - 1
            else:
                left = pivot_index + 1


    def randomIndex(self, left, right):
        return random.randint(left, right)
    
    def partitionAndReturnIndex(self, nums, pivotIndex, left, right):
        pivot = nums[pivotIndex]
        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
        ind = left + 1

        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                nums[ind], nums[i] = nums[i], nums[ind]
                ind += 1
        nums[left], nums[ind -1] = nums[ind -1], nums[left]
        return ind - 1


nums = [3,2,1,5,6,4]
k = 2
s = Solution()
print(s.findKthLargest(nums, k))

"""
Time complexity:O(n)
Worst case (e.g., sorted input, bad pivot): O(n²)

Space complexity: O(1)
"""