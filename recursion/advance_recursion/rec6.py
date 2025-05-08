"""
Combination Sum
39
"""

def backtrack(index, total, subset):
    print(index, total, subset)
    if total == 9:
        print("subset", subset)
        result.append(subset.copy())
        return
    if total > 9:
        return
    elif index >= len(nums):
        return
    subset.append(nums[index])
    sum1 = total + nums[index]
    backtrack(index, sum1, subset)

    subset.pop()
    sum1 = total
    backtrack(index+1, sum1, subset)

nums = [5 ,9,4, 3]
result = []
k = 9
backtrack(0,0, [])
print(result)