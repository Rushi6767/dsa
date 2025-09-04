"""
796. Rotate String
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(s)

        # O(n)
        for i in range(n):
            # O(n) slicing
            res = s[-1] + s[:-1]
            if res == goal:
                return True
            s = res
        return False

s = "abcde"
goal = "cdeab"
sol = Solution()
# print(sol.rotateString(s, goal))

"""
Time Complexity : O(n^2)
Space Complexity : O(n)
"""


# optimal solution

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # O(n)
        double_string = s + s

        # O(n)
        if goal in double_string:
            return True
        else:
            return False

s = "abcde"
goal = "cdeab"
sol = Solution()
print(sol.rotateString(s, goal))

"""
Time Complexity : O(n+n) == O(2n) == O(n)
Space Complexity : O(2n) == O(n)
"""