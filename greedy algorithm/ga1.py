"""
Fractional knapsack
"""

a = [(100,20), (60,10), (100,50), (200,50)]
w = 90
a.sort(key=lambda x: x[0] / x[1], reverse=True)
print(a)
n = len(a)

final_value = 0
currrent_value = 0

for i in range(n):
    if currrent_value + a[i][1] < w:
        currrent_value += a[i][1]
        final_value += a[i][0]
    else:
        remain = w - currrent_value
        cost = a[i][0]//a[i][1] * remain
        final_value += cost
        break

print(final_value)

"""
Time complexity : O(nlogn) + O(n)
Space complexity : O(1)
"""