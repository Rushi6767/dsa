"""
Count the occurance of a number
"""
# nums = [1,3,3,3,5,6]
# target = 3
# n = len(nums)
# first = -1
# last = -1

# for i in range(n):
#     if nums[i] == target:
#         if first == -1:
#             first = i
#         last = i
# if first == -1:
#     total = 0
# else:
#     total = last+1 - first
# print(total)

def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    lb = -1

    while low <= high:
        mid = (low + high)//2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

def upper_bound(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    lb = n

    while low <= high:
        mid = (low + high)//2

        if nums[mid] > target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

nums = [1,3,3,3,5,6]
target = 3
# print(upper_bound(nums, target))

first = lower_bound(nums, target)
last = upper_bound(nums, target)

total = last - first
print(total)

"""
Time Complexity: O(2logn) == O(logn)
Space Complexity: O(1)
"""