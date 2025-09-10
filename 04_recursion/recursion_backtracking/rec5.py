"""
Reverse an Array Using While Loop
"""


# num = [1,2,3,4,5,6,7]
# left = 0
# right = 6

# while left < right:
#     print("l",left, "r", right)
#     num[left], num[right] = num[right], num[left]
#     left+=1
#     right-=1
# print(num)


"""
Reverse an Array Using Recursion
"""


# def rev_a(num, l, r):
#     if l > r:
#         return num
#     else:
#         print("l",l, "r", r)
#         num[l], num[r] = num[r], num[l]
#         l+=1
#         r-=1
#         return rev_a(num, l, r)

# # num = [5,7,3,2,6,1,5,9]
# num = [1,2,3,4,5,6,7]
# left = 0
# right = 6
# print(rev_a(num, left, right))



# ====================================================
def rev_a(num, l, r):
    if l > r:
        return num
    else:
        print("l",l, "r", r)
        num[l], num[r] = num[r], num[l]
        return rev_a(num, l+1, r-1)

num = [1,2,3,4,5,6,7]
left = 0
right = 6
print(rev_a(num, left, right))


"""
Time complexity: O(n/2) == O(n)
Space complexity: O(n/2) == O(n) which is Stack Space
"""