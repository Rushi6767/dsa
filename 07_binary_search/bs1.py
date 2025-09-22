"""
Binary Search
"""
# ===Iterative solution=============
# always use this solution.

def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1

    while low<=high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
    return -1

nums = [2,4,6,7,9,11,18,19]
target = 19
print(binary_search(nums, target))

# ==recursive for understanding==========
# def binary_search(low, high):
#     if low > high:
#         return -1
#     mid = (low + high)//2        
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         return binary_search(mid+1, high )  
#     elif nums[mid] > target:
#         return binary_search(mid, high-1)

# nums = [2,4,6,7,9,11,18,19]
# target = 11
# n = len(nums)
# low = 0
# high = n-1

# print(binary_search(low, high))


"""
Time Complexity: O(log2(n)) ;where n is number of elements
Space Complexity: O(1)
"""