"""
1, Selection sort
"""
nums = [5,7,8,4,1,6,9,2]

for i in range(len(nums)):
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    nums[i] , nums[min_index] = nums[min_index], nums[i]

print(nums)            

"""
tc == O(n**2)
sc == O(1)
"""


# ======desnding order========================

# nums = [5,7,8,4,1,6,9,2]

# for i in range(len(nums)):
#     min_index = i
#     for j in range(i+1, len(nums)):
#         if nums[min_index] < nums[j]:
#             min_index = j
#     nums[i] , nums[min_index] = nums[min_index], nums[i]

# print(nums)            