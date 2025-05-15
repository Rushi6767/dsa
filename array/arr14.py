"""
2149. Rearrange Array Elements by Sign
"""

# nums = [3,1,-2,-5,2,-4]
# n = len(nums)
# # nums = [-1,1]
# result = []
# r1 =[]
# r2 =[]

# for i in nums:
#     if i > 0:
#         r1.append(i)
#     else:
#         r2.append(i)

# print(r1)
# print(r2)

# for i in range(n//2):
#     result.append(r1[i])
#     result.append(r2[i])

# print(result)

# nums = [3,1,-2,-5,2,-4]
# n = len(nums)
# r1 =[]
# r2 =[]

# for i in nums:
#     if i > 0:
#         r1.append(i)
#     else:
#         r2.append(i)

# for i in range(n//2):
#     nums[(i*2)] = r1[i]
#     nums[(i*2)+1] = r2[i]

# print(nums)
"""
Time complexity: O(n + (n/2))
Space complexity: O((n/2) + (n/2)) ==== O(n)
"""

nums = [3,1,-2,-5,2,-4]
l = len(nums)
result = [0] * l

p = 0
n = 1

for i in range(l):
    if nums[i] > 0:
        result[p] = nums[i]
        p+=2
    else:
        result[n] = nums[i]
        n+=2
print(result)

"""
Time complexity: O(n)
Space complexity: O(1)  / O(n) 
depends tell O(1) take and return result
"""