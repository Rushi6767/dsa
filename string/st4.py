"""
14. Longest Common Prefix
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        base = strs[0]
        result = ""

        for i in range(len(base)):
            for j in strs[1:]:
                if i == len(j) or j[i] != base[i]:
                    return result
            result = result + base[i]
        return result


strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))

"""
Time Complexity : O(n X m)
Space Complexity : O(m) == O(1)
in== result, out == result
"""