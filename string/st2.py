"""
151. Reverse Words in a String
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return " ".join(arr[::-1])
    
s = "  hello world  "
sol = Solution()
# print(sol.reverseWords(s))

"""
O(3n) = split, join, reverse
Time Complexity : O(3n) = O(n)
Space Complexity : O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        res = ""
        for i in arr:
            res = i + " " + res
        return res.strip()
    
s = "a good   example"
sol = Solution()
print(sol.reverseWords(s))