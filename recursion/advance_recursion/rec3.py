"""
Count all subsequences with sum k
"""
def backtracking(index, total):
    if total == k:
        return 1
    elif total > k:
        return 0
    
    if index >= len(nums):
        return 0
    sum1 = total + nums[index]
    pick = backtracking(index+1, sum1)

    sum1 = total
    unpick = backtracking(index+1, sum1)
    return pick + unpick

nums = [5,9,4]
k = 9
print(backtracking(0,0))
