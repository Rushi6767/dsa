"""
34. Find First and Last Position of Element in Sorted Array
"""

# nums = [5,7,7,8,8,10]
# target = 8
# n = len(nums)
# first = -1
# last = -1

# for i in range(n):
#     if nums[i] == target:
#         if first == -1:
#             first = i
#         last = i
#     elif nums[i] > target:
#         break

# print(first, last)

# optimal

from typing import List

class Solution:
    def binarySearchLeft(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1  # Default index if target is not found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid  # Update index and continue searching left
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    def binarySearchRight(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1  # Default index if target is not found

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid  # Update index and continue searching right
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ext_left = self.binarySearchLeft(nums, target)
        if ext_left == -1:
            return [-1, -1]  # If first occurrence is not found, target does not exist
        
        ext_right = self.binarySearchRight(nums, target)
        return [ext_left, ext_right]

"""
Time Complexity: O(2logn) == O(logn)
Space Complexity: O(1)
"""