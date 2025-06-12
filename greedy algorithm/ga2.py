"""
Minimum number of coins
"""

# coins = [1,2,5,10,20,50,100,200,500,2000]
# w = 43
# w = 57
# n = len(coins)
# result = []

# while w != 0:
#     for i in range(n):
#         if coins[i] > w:
#             w = w - v
#             break
#         v = coins[i]
#     result.append(v)

# print(result)

coins = [1,2,5,10,20,50,100,200,500,2000]
w = 43
n = len(coins)
result = []

for i in range(n-1, -1,-1):
    while w >= coins[i] :
        result.append(coins[i])
        w -= coins[i]
print(result)

"""
Time complexity : O(w)
Space complexity : O(1)
"""