"""
1004. Max Consecutive Ones III
"""
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# n = len(nums)
# maxi = 0

# for i in range(n):
#     zeros = 0
#     for j in range(i, n):
#         if nums[j] == 0:
#             zeros += 1
#         if zeros > k:
#             break
#         maxi = max(maxi, j-i+1)

# print(maxi)
"""
Time complexity: O(n(n+1)/2) == O(n^2)
Space complexity: O(1)
"""

# ==better=============
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# n = len(nums)
# left =0
# right =0
# maxi = 0
# zeros = 0

# while right < n:
#     if nums[right] == 0:
#         zeros += 1
#     while zeros > k:
#         if nums[left] == 0:
#             zeros -= 1
#         left += 1
#     maxi = max(maxi, right-left+1)
#     right += 1

# print(maxi)

"""
Time complexity: O(n) + O(n) == O(2n)
Space complexity: O(1)
"""

# =====optimal=========
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left =0
        right =0
        maxi = 0
        zeros = 0

        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                maxi = max(maxi, right-left+1)
            right += 1

        return maxi
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
s = Solution()
print(s.longestOnes(nums, k))

"""
Time complexity: O(n)
Space complexity: O(1)
"""
