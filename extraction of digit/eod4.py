"""
Armstrong number
"""
from math import *

n = 1634
num =n
# length = int(str(n))
length = floor(log10(n) + 1)
arm = 0

while n > 0:
    a = n % 10
    arm = arm + a ** length
    n = n//10

print(arm)
print(num == arm)

"""
Thngs which is divideable by 10 ==> log10(N)

time complexity : O(log10(N))
space complexity : O(1)
"""