"""
416. Partition Equal Subset Sum
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 == 1:
            return False

        target = target//2

        prev = [False for _ in range(target + 1)]
        prev[0] = True  # sum 0 is always achievable

        if nums[0] <= target:
            prev[nums[0]] = True

        for index in range(1, n):
            curr = [False for _ in range(target + 1)]
            curr[0] = True  # sum 0 always achievable
            for t in range(1, target + 1):
                if nums[index] > t:
                    pick = False
                else:
                    pick = prev[t - nums[index]]
                not_pick = prev[t]
                curr[t] = pick or not_pick
            prev = curr  # move window

        if prev[target] == True:
            return True
        return False
