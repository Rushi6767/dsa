"""
Check if subsequences of k is exists or not
"""

# def backtrack(index, total, subset):
#     if total==9:
#         result.append(subset.copy())
#         return True
#     elif total > 9:
#         return False

#     if index >= len(nums):
#         return False
          
#     subset.append(nums[index])
#     sum1 = total + nums[index]
#     pick = backtrack(index+1, sum1, subset)

#     if pick==True:
#         return True
#     e = subset.pop()
#     sum1 = total
#     not_pick = backtrack(index+1, sum1, subset)
#     return not_pick

# nums = [5,9,4]
# result = []
# print(backtrack(0, 0, []))
# print(result)



# ============================Second Method===============================================
def backtrack(index, total):
    if total==k:
        return True
    elif total > k:
        return False

    if index >= len(nums):
        return False
          
    sum1 = total + nums[index]
    pick = backtrack(index+1, sum1)

    if pick==True:
        return True
    sum1 = total
    not_pick = backtrack(index+1, sum1)
    return not_pick

# k=30
k=9
nums = [5,9,4]
print(backtrack(0, 0))
