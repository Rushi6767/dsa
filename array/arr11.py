"""
Two sum problem
"""

# nums = [5,9,1,2,4,15,6,3]
# target = 13
# n = len(nums)
# result = []

# for i in range(n):
#     for j in range(i,n):
#         add = nums[i] + nums[j]
#         if add == target:
#             result.append([nums[i], nums[j]])

# print(result)

"""
Time complexity: O(n(n+1)//2) == O(n^2)
Space complexity: O(1)
"""


# nums = [5,9,1,2,4,15,6,3,10]
# nums = [2,7,11,15]
nums = [3,2,4]
target = 6
n = len(nums)
result = []
d = {}

for i in range(n):
    r = target - nums[i]

    if r in d:
        # result.append([nums[d[r]], nums[i]])
        result.append([d[r], i])
    d[nums[i]] = i
    
print(result)

"""
Time complexity: O(n)
Space complexity: O(n)
"""