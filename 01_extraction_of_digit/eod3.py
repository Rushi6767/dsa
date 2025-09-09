"""
Check if Number is Palidrome or not
"""

n = 1234
num = n
r = 0

while n>0:
    a = n % 10
    r = r * 10 + a
    n = n //10

print(r)
print(num == r)

"""
Thngs which is divideable by 10 ==> log10(N)

time complexity : O(log10(N))
space complexity : O(1)
"""