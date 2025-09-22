"""
81. Search in Rotated Sorted Array II
"""

def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True
        
        if nums[low] == nums[mid] == nums[high]:
            low = low + 1
            high = high -1
            continue

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
    return False


nums = [1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
print(binary_search(nums, target))

"""
Time Complexity: 
Average case: O(logn)
Worst case: O(n/2)

Space Complexity: O(1)
"""   