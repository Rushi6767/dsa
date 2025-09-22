"""
35. Search Insert Position (lower bound)
"""

def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    lb = n

    while low <= high:
        mid = (low + high)//2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

nums = [1,3,5,6]
target = 7
print(binary_search(nums, target))

"""
Time Complexity: O(log2(n)) ;where n is number of elements
Space Complexity: O(1)
"""    

# ==brute force
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in nums:
#             if i >= target:
#                 return nums.index(i)
#         return len(nums)

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""