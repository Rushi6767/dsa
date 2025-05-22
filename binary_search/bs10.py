"""
Find minimum in rotated sorted array
"""

def binary_search(nums):
    n = len(nums)
    low = 0
    high = n-1
    mini = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] <= nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1

        else:
            mini = min(mini, nums[low])
            low = mid + 1
            
    return mini


nums = [4,5,6,7,8,9,10,0,1,2]
print(binary_search(nums))

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""        