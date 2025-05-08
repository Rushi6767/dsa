"""
Count the number of Digit in a integer
"""

n = 5873111111111
count = 0

while n > 0:
    a = n%10
    n = n//10
    count += 1
print(count)

# # =========================
# n = 5873111111111
# print(len(str(n)))

# ==============================
from math import *
# print("log",log10(567))

# print(floor(log10(5837) + 1))

"""
Thngs which is divideable by 10 ==> log10(N)

time complexity : O(log10(N))
space complexity : O(1)
"""