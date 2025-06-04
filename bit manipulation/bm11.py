"""
78. Subsets
"""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subset = 1<<n
        result = []

        for num in range(0, total_subset):
            lst = []
            for i in range(0,n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
            result.append(lst)
        return result
"""
Time complexity : O(n x (2^n))
Space complexity: O((2^n) x n)
"""