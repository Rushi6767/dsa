"""
Greedy algorithm
455. Assign Cookies
"""
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        left = 0
        right = 0
        c = 0

        while left<n and right<m:
            if g[left] <= s[right]:
                c += 1
                left += 1
            right += 1

        return c
    
g = [2,6,8,1,4]
s = [4,2,7,1,2,3]
s1 = Solution()
print(s1.findContentChildren(g,s))

"""
Time complexity : O(nlogn) + O(mlogm) + O(m)
Space complexity : O(1)
"""