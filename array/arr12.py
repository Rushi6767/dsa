"""
53. Maximum subarray
"""
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# n = len(nums)
# total = 0
# maxi = float("-inf")

# for i in range(n):
#     total = 0
#     for j in range(i,n):
#         total = total + nums[j]
#         if maxi < total:
#             maxi = total

# print(maxi)

"""
Time complexity: O(n(n+1)//2) == O(n^2)
Space complexity: O(1)
"""


nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
total = 0
maxi = float("-inf")

for i in range(n):
    total = total + nums[i]
    maxi = max(maxi, total)

    if total < 0:
        total = 0
print(maxi)

"""
Time complexity: O(n)
Space complexity: O(1)
"""