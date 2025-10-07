"""
20. Valid Parentheses
"""

def is_valid(s):
    stack = []
    for bracket in s:
        if bracket=="(" or bracket=="[" or bracket=="{":
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            e = stack.pop()
            if (
                (bracket == ")" and e == "(") or
                (bracket == "]" and e == "[") or
                (bracket == "}" and e == "{") 
            ):
                continue
            else:
                return False
    return len(stack) == 0

print(is_valid("(())"))

"""
Time complexity :O(n)
Space complexity :O(n)
"""