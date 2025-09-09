"""
Print Factor/Divisor
"""

# n = 15
# l =[]

# for i in range(1,n+1):
#     if n % i == 0:
#         l.append(i)

# print(l)

# """
# time complexity : O(N)
# space complexity : O(k)
# where k; k would the total number of factors
# """


# # ==optimal solution========================================
# """
# notice: we can run loop half
# after half loop we can not get divisors except last element which number it self
# """

# n = 15
# l=[]

# for i in range(1, n//2):
#     if n % i ==0:
#         l.append(i)
# l.append(n)
# print(l)
        
# """
# time complexity : O(N/2) which almost O(N)
# space complexity : O(k)
# where k; k would the total number of factors
# """

# ==More optimal solution===========================================
"""
Notice:n=36
1 ==> 36
2 ==> 18
3 ==> 12
4 ==> 9
6 ==> 6

go till square root
"""

from math import sqrt
n = 36
l =[]

for i in range(1, int(sqrt(n))+1):
    print(i)
    if n % i == 0:
        l.append(i)
        if n//i != i:
            l.append(n//i)
print(l)

"""
time complexity : O(sqrt(n))
if answer in sort form so, time complexity : O(sqrt(n)) + O(nlogn)
space complexity : O(k)
where k; k would the total number of factors
"""