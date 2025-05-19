"""
Lower bound : smallest index such that nums[i] >= target
"""

def binary_serch(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    lower_b = n

    while low <= high:

        mid = (low + high)//2
        if nums[mid] >= target:
            lower_b = mid
            high = mid - 1
        
        else:
            low = mid + 1
    return lower_b
            

nums = [1,1,1,1,2,2,2,3,4,5,5,6,7,7,7,8,8,9,12,12,13]
target = 20
print(binary_serch(nums, target))

"""
Time Complexity: O(log2(n)) ;where n is number of elements
Space Complexity: O(1)
"""