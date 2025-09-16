"""
Find the second largest Element
"""

# nums= [55,32,97,-55, 45,32,88,21]
# nums.sort()
# print(nums[-2])
"""
Time complexity : O(nlogn)
Space complexity : O(1)
"""

# nums= [55,32,97,-55, 45,32,88,21]
# # large  = float("-inf")
# large  = nums[0]
# s_large = nums[0]
# for i in nums:
#     if large< i:
#         large = i

# # print(large)
# for i in nums:
#     if s_large< i and i != large:
#         s_large = i
# print(s_large)

"""
Time complexity : O(n+n) === O(2n) === O(n)
Space complexity : O(1)
"""

nums= [55,32,97,-55, 45,32,88,21]
large  = float("-inf")
s_large = float("-inf")

for i in nums:
    if large< i:
        s_large = large
        large = i
    elif i > s_large and i != large:
        s_large = i 

print(s_large)

"""
Time complexity : O(n)
Space complexity : O(1)
"""