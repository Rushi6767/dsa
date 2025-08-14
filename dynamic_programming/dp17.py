"""
Count Partitions with Given Difference 
"""

def fun(index, total):
    if index == 0:
        if total == 0 and arr[0] == 0:
            return 2
        
        if total == 0 or arr[0] == total:
            return 1
        return 0

    if arr[index] > total:
        pick = 0
    pick = fun(index - 1, total - arr[index])
    not_pick = fun(index - 1, total)

    return pick + not_pick

arr = [5,2,6,4]
target = 30
n = len(arr)
total = sum(arr)
# if (total - target) < 0 or (total - target) % 2 == 1:
#     print(0)
# print(fun(n-1, (total - target)//2))


"""
Tabulation with space optimization
"""

def fun(arr, target):
    n = len(arr)
    prev = [0 for _ in range(target + 1)]

    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1
        if arr[0] <= target:
            prev[arr[0]] = 1

    for index in range(1, n):
        curr = [0 for _ in range(target + 1)]
        for total in range(target + 1):
            pick = 0
            if arr[index] <= total:
                pick = prev[total - arr[index]]
            not_pick = prev[total]
            curr[total] = pick + not_pick
        prev = curr

    return prev[target]

def countPartition(arr, d):
    total = sum(arr)
    if (total - d) < 0 or (total - d) % 2 == 1:
        return 0
    target = (total - d) // 2
    return fun(arr, target)

arr = [5, 2, 6, 4]
d = 3
print(countPartition(arr, d))
