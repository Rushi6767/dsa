"""
55. Jump Game
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_index = 0

        for i in range(n):
            if i > max_index:
                return False
            max_index = max(max_index, i+nums[i])
        return True
        
nums = [3,2,1,0,4]
s = Solution()
print(s.canJump(nums))

"""
Time complexity : O(n)
Space complexity : O(1)
"""