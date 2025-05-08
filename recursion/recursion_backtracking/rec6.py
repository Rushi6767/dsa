"""
Check String is Palidrome or not
"""

# def pali(s):
#     if len(s) < 1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return pali(s[1:-1])
#         else:
#             return False

# s = "nitin"
# print(pali(s))

"""
Check String is Palidrome or not with looping
"""

# s= "moom"
# left = 0
# right = len(s)-1


# while left < right:
#     if s[left] != s[right]:
#         return False
#     left+=1
#     right-=1
# return True



def pali(s, left, right):
    if left > right:
        return True
    else:
        print(s[left], s[right])
        if s[left] != s[right]:
            return False
        else:
            return pali(s, left+1, right-1)

s = "moom"
left = 0
right = len(s) - 1
print(pali(s, left, right))