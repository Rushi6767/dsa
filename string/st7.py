"""
242. Valid Anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            # 2 x nlog(n)
            if sorted(s) == sorted(t):
                return True
            else:
                return False
        else:
            return False

s = "anagram"
t = "nagaram"
sol = Solution()
# print(sol.isAnagram(s, t))

"""
Time Complexity : O(2 x nlog(n)) == O(nlog(n))
Space Complexity : O(2n) == O(n)
"""



# my solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            n = len(s)
            ds = {}
            dt = {}
            for i in range(n):
                ds[s[i]] = ds.get(s[i], 0) + 1
                dt[t[i]] = dt.get(t[i], 0) + 1
            return ds == dt
        else:
            return False

s = "anagram"
t = "nagaram"
sol = Solution()
# print(sol.isAnagram(s, t))

# optimized
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        # O(n)
        for ch in s:
            chars[ch] = chars.get(ch, 0) + 1

        # O(n)
        for ch in t:
            # O(1)
            if ch not in chars:
                return False
            # O(1)
            else:
                if chars[ch] == 0:
                    return False
                chars[ch] -= 1
        return True
    
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))

"""
Time Complexity : O(n + n) == O(2n) = O(n)
Space Complexity : O(26) == O(1)
"""

"""
this solution is best because
It uses only one dictionary (less space).
It can exit early when it detects a mismatch (faster in worst-case scenarios).
"""