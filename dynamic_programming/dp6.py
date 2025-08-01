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
print(func(1, 3))

"""
Time complexity : O(3^n)
Space complexity : O(n)
"""