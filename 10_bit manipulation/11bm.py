"""
136. Find the single number
"""
# nums = [5,1,3,3,1,7,7,5,8]
# d = {}

# for i in nums:
#     d[i] = d.get(i, 0) + 1

# for j in d:
#     if d[j] == 1:
#         print(j)

"""
Time complexity : O(n) + O((n/2) + 1) == O(n)
Space complexity: O(n/2)
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result = result^i
        return result
    
"""
Time complexity : O(n)
Space complexity: O(1)
"""
