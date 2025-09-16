"""
Right Rotate Array by k place
"""
# nums = [3,9,5,6,7,2]
# k = 3
# nums[:] = nums[-k:] + nums[:-k]
# print(nums)

# ==optimal
nums = [3,9,5,6,7,2]
k = 3
rotation = k%len(nums)
nums[:] = nums[-rotation:] + nums[:-rotation]
print(nums)

"""
Time complexity : O(n)
Space complexity : O(1)
"""

# nums = [3,9,5,6,7,2]
# k = 3
# n = len(nums)


# for _ in range(k):
#     temp = nums[-1]
#     for i in range(n-2, -1, -1):
#         nums[i+1] = nums[i]

#     nums[0] = temp
# print(nums)

# ===new solution===

# nums = [3,9,5,6,7,2]
# k = 3
# n = len(nums)
# rotation = k % n

# for _ in range(rotation):
#     # O(r)
#     e = nums.pop()
#     # O(1)
#     nums.insert(0, e)
#     # O(n)
    
# print(nums)

"""
Time complexity : O(rxn)
Space complexity : O(1)
"""


# def reverse(nums, left, right):
#     while left > right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left +=1
#         right -= 1

# nums = [3,9,5,6,7,2]
# n = len(nums)
# k = 3
# reverse(nums, n-k, n-1)
# reverse(nums, 0,n-k-1)
# reverse(nums,0, n-1)
# """
# Time complexity : O(n)
# Space complexity : O(1)
# """