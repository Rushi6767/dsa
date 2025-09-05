"""
1614. Maximum Nesting Depth of the Parentheses
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        c = 0
        maxi = 0

        for i in s:
            if i == "(":
                c+=1
            elif i == ")":
                c-=1
            maxi = max(maxi, c)
        return maxi


s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
print(sol.maxDepth(s))

"""
Time Complexity : O(n)
Space Complexity : O(d) where d is maximum depth of bracket
"""



class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        c = 0
        maxi = 0

        for i in s:
            if i != "(" and i != ")":
                continue
            if i == "(":
                c+=1
            elif i == ")":
                c-=1
            maxi = max(maxi, c)
        return maxi


s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
# print(sol.maxDepth(s))