"""
33. Search in Rotated Sorted Array
"""

def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] <= nums[high]:
            if nums[mid]<= target <= nums[high]:
                low = mid + 1
            else:
                high = mid -1

        else:
            if nums[low]<= target <= nums[mid]:
                high = mid -1
            else:
                low = mid + 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(binary_search(nums, target))

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""        