"""
1021. Remove Outermost Parentheses
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        c = 0

        for i in s:
            if i == "(":
                if c != 0:
                    stack.append(i)
                c += 1
            else:
                c -= 1
                if c!= 0:
                    stack.append(i)

        return "".join(stack)
        
s1 = Solution()
s = "(()())(())(()(()))"
# print(s1.removeOuterParentheses(s))



"""
with using of string
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        c = 0

        for i in s:
            if i == "(":
                if c != 0:
                    result += i
                c += 1
            else:
                c -= 1
                if c!= 0:
                    result += i

        return result
        
s1 = Solution()
s = "(()())(())(()(()))"
print(s1.removeOuterParentheses(s))

"""
Time Complexity : O(n)
Space Complexity : O(1)
"""