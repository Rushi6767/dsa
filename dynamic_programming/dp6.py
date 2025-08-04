"""
Geek's trainning
with 2d array
"""

def func(day, last):
    if day == 0:
        maxi = 0
        for i in range(0, 3):
            if i != last:
                maxi = max(maxi, arr[day][i])
        return maxi

    maxi = 0
    for i in range(0, 3):
        if i != last:
            maxi = max(maxi, arr[day][i] + func(day-1, i))
    return maxi

arr = [[1, 60, 40], [50, 130, 70]]
# print(func(1, 3))

"""
Time complexity : O(3^n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""
def func(day, last, dp):
    if day == 0:
        maxi = 0
        for i in range(0, 3):
            if i != last:
                maxi = max(maxi, arr[day][i])
        return maxi
    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for i in range(0, 3):
        if i != last:
            maxi = max(maxi, arr[day][i] + func(day-1, i, dp))
    dp[day][last] = maxi
    return dp[day][last]

arr = [[1, 60, 40], [50, 130, 70]]
n = len(arr)
dp = [[-1] * 3 for _ in range(n)]
# print(func(n-1, 2, dp))

"""
Time complexity : O(n x 4 x 3)
Space complexity : O(n) + O(4n)
stack space + dp space
"""

"""
3. Tabulation [Bottom - Up]
"""

n = len(arr)
# DP table: n days x 4 last tasks
dp = [[-1 for _ in range(4)] for _ in range(n)]
# Init day 0 for each possible last
dp[0][0] = max(arr[0][1], arr[0][2])
dp[0][1] = max(arr[0][0], arr[0][2])
dp[0][2] = max(arr[0][0], arr[0][1])
dp[0][3] = max(arr[0][0], arr[0][1], arr[0][2])
# Fill for each day
for day in range(1, n):
    for last in range(0, 4):
        maxi = 0
        for i in range(0, 3):
            if i != last:
                maxi = max(maxi, arr[day][i] + dp[day - 1][i])
        dp[day][last] = maxi
# print(dp[n - 1][3])

"""
Time complexity : O(n X 4 X 3)
Space complexity : O(4n)
"""

"""
4. Tabulation (Space Optimation)
"""
n = len(arr)
# Prev row for space opt
prev = [-1 for _ in range(4)]
# Init for day 0
prev[0] = max(arr[0][1], arr[0][2])
prev[1] = max(arr[0][0], arr[0][2])
prev[2] = max(arr[0][0], arr[0][1])
prev[3] = max(arr[0][0], arr[0][1], arr[0][2])
# For each day
for day in range(1, n):
    curr = [-1 for _ in range(4)]
    for last in range(0, 4):
        maxi = 0
        for i in range(0, 3):
            if i != last:
                maxi = max(maxi, arr[day][i] + prev[i])
        curr[last] = maxi
    # Update prev to curr
    prev = curr.copy()
print(prev[3])

"""
Time complexity : O(n X 4 X 3)
Space complexity : O(1)
"""