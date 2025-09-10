"""
Topic : parameterized & Function Recursion

Task : Sum of 1 to N
"""
# parameter way

# def sum(s, i, n):
#     if i > n:
#         print(s)
#         return
    
#     sum(s+i, i+1, n)

# sum(0, 1, 5)


#  Function Recursion
def sum(n):
    if n==0:
        return n
    return n + sum(n-1)

print(sum(10))

"""
Time complexity: O(n)
Space complexity: O(n) which is Stack Space
"""