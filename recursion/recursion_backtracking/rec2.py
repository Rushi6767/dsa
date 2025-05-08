"""
topic: Recursion using parameter
print x n times
"""


# def rus(n, x):
#     if n == 0:
#         return
#     print(x)
#     n-=1
#     rus(n, x)

# rus(4, 67)


def rus(n, x):
    if n == 0:
        return 
    print(x)
    rus(n-1, x)

rus(4, 67)