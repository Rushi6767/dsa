"""
2. Bubble Sort
"""

nums= [5,8,1,6,9,2,4]

for i in range(len(nums)-2, -1, -1):
    for j in range(0, i+1):
        if nums[j] > nums[j+1]:
            nums[j] , nums[j+1] = nums[j+1], nums[j]
print(nums)


"""
Time complexity: O(n**2)
Space Complexity: O(1)
"""


# ===Decendic Order====================

# nums= [5,8,1,6,9,2,4]

# for i in range(len(nums)-2, -1, -1):
#     for j in range(0, i+1):
#         if nums[j] < nums[j+1]:
#             nums[j] , nums[j+1] = nums[j+1], nums[j]
# print(nums)


# # ==for best case===============
# nums= [5,8,1,6,9,2,4]

# for i in range(len(nums)-2, -1, -1):
#     is_swap = False
#     for j in range(0, i+1):
#         if nums[j] > nums[j+1]:
#             nums[j] , nums[j+1] = nums[j+1], nums[j]
#     if is_swap == False:
#         break
# print(nums)


# """
# Time complexity: O(n)
# Space Complexity: O(1)
# """