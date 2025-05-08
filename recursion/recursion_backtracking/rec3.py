"""
print 1 to n with recursion
"""

# def rus(i, n):
#     if i>n:
#         return
#     print(i)
#     rus(i+1, n)

# rus(1, 10)

# def rus(i, n):
#     if i>n:
#         return
#     rus(i+1, n)
#     print(i)

# rus(1, 10)


# # head
# def rus(n):
#     if n==0:
#         return
#     print(n)
#     rus(n-1)

# rus(10)


"""
hw: do 1 to n with tail recursion
"""

def rus(n):
    if n==0:
        return
    rus(n-1)
    print(n)

rus(5)