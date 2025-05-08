"""
Generate subsequence with sum k
"""

# def func(index, subset):
#     if index >= len(nums):
#         print(sum(subset))
#         if sum(subset) == 9:
#             result.append(subset.copy())
#         return
#     subset.append(nums[index])
#     func(index+1, subset)
#     subset.pop()
#     func(index+1, subset)

# nums = [9,5,7,4]
# result = []
# func(0, [])
# print(result)


# def func(index, total, subset):
#     print(index, total)
#     if index >= len(nums) or total >= 9:
#         if total==9:
#             result.append(subset.copy())
#         return
#     subset.append(nums[index])
#     total+=nums[index]
#     func(index+1, total, subset)
#     subset.pop()
#     total-=nums[index]
#     func(index+1, total, subset)

# nums = [5,9,4]
# result = []
# func(0,0, [])
# print(result)



# def backtrack(index, total, subset):
#     if total == k:
#         result.append(subset.copy())
#         return
#     elif total > k:
#         return
#     if index >= len(nums):
#         return
#     subset.append(nums[index])
#     sum1 = total + nums[index]
#     backtrack(index+1, sum1, subset)
#     e = subset.pop()
#     sum1 = sum1 - e
#     backtrack(index+1, sum1, subset)

# nums = [5,9,4]
# result = []
# k = 9
# backtrack(0,0, [])
# print(result)




def backtrack(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    total += nums[index]
    backtrack(index+1, total, subset)
    subset.pop()
    total -= nums[index]
    backtrack(index+1, total, subset)

nums = [5,9,4]
result = []
k = 9
backtrack(0,0, [])
print(result)