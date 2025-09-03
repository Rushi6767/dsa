"""
205. Isomorphic Strings
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        d1 = {}

        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            
            else:
                d[s[i]] = t[i]

            if t[i] in d1:
                if d[t[i]] != s[i]:
                    return False
            
            else:
                d[s[i]] = t[i]

        return True

# s = "egg"
# t = "add"

# s = "foo"
# t = "bar"

s = "badc"
t = "baba"

s = "paperpe"
t = "titlesl"
sol = Solution()
print(sol.isIsomorphic(s, t))

"""
Time Complexity : O(n)
Space Complexity : O(2n) == O(n)
"""