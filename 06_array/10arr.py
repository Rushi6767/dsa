"""
Find the missing number
"""

# num = [1,0,3,4]
# n = len(num)

# # O(n)
# for i in range(n+1):
#     # O(n)
#     if i not in num:
#         print(i)

"""
Time complexity: O(n^2)
Space complexity: O(1)
"""




# from typing import List
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)

#         for i in range(n+1):
#             if i not in nums:
#                 return i

# nums = [0,1]
# s = Solution()
# print(s.missingNumber(nums))


# num = [1,0,3,4]
# n = len(num)
# d = {}

# # O(n)
# for i in range(n+1):
#     # O(n)
#     d[num.count(i)] = i
# print(d[0])
"""
Time complexity: O(n^2)
Space complexity: O(1)
"""


# nums = [1,0,3,4]
# n = len(nums)
# d = {}

# # O(n)
# for i in range(n+1):
#     d[i] = 0

# for num in nums:
#     d[num] = 1

# for k,v in d.items():
#     if v == 0:
#         print(k)
# print(d)
"""
Time complexity: O(3n) ===  O(n)
Space complexity: O(n)
"""


from typing import List

def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

nums = [1,0,3,4]
print(missingNumber(nums))
"""
Time complexity: O(n)
Space complexity: O(1)
"""