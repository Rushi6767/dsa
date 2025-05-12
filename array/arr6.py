"""
Move zero to the end
"""

# nums = [1,0,2,4,3,0,0,3,5,1]
# temp =[]
# cl = [0] * nums.count(0)

# for i in range(len(nums)):
#     if nums[i] !=0:
#         temp.append(nums[i])

# nums[:] = temp + cl
# print(nums)

"""
Time complexity : O(n)
Space complexity : O(n)
"""


# nums = [1,0,2,4,3,0,0,3,5,1]
# j = 0

# for i in range(len(nums)):
#     if nums[i] !=0:
#         # temp.append(nums[i])
#         nums[j] = nums[i]
#         j+=1
# # print(nums)
# # print(j)

# for t in range(j, len(nums)):
#     nums[t] = 0

# print(nums)

"""
Time complexity : O(n)
Space complexity : O(1)
"""


# nums = [1,0,2,4,3,0,0,3,5,1]
# j = 0
# n = len(nums)
# for i in range(0,n):
#     if nums[i] != 0:
#         nums[j], nums[i] = nums[i], nums[j]
#         j += 1

# print(nums)
"""
Time complexity : O(n)
Space complexity : O(1)
"""


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         if len(nums) == 1:
#             return
#         i = 0
#         while i < len(nums):
#             if nums[i] == 0:
#                 break
#             i += 1
#         else:
#             return
#         j = i + 1
#         while j < len(nums):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#             j += 1