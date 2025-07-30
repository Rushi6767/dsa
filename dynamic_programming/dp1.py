"""fibonacci"""

"""
1. Recursion [Top - Down]
"""

def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fib(num - 1) + fib(num - 2)

# print(fib(6))
"""
Time complexity : O(2^n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""

def fib(num, dp):
    if num <= 1:
        return num
    
    if dp[num] != -1:
        return dp[num]
   
    dp[num] = fib(num - 1, dp) + fib(num - 2, dp)
    return dp[num]

n = 5
dp = [-1] * (n+1)
# print(fib(n, dp))

"""
Time complexity : O(n)
Space complexity : O(n) + O(n)
"""

"""
3. Tabulation [Bottom - Up]
"""

n = 5
dp = [0] * (n+1)

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# print(dp)
# print(dp[n])

"""
Time complexity : O(n)
Space complexity : O(n)
"""

"""
4. Tabulation (Space Optimation)
"""
n = 5
prev2 = 0
prev = 1

for i in range(2, n+1):
    curr = prev + prev2
    prev2 = prev
    prev = curr

print(prev)
print(curr)
# Note : always return prev (Good Practice)
"""
Time complexity : O(n)
Space complexity : O(1)
"""