"""
Combination of sum 3
"""

# def backtrack(index, total, subset):
#     if total == n:
#         if len(subset) == k:
#             result.append(subset.copy())
#         return
#     elif total > n:
#         return

#     if index == len(nums):
#         return

#     subset.append(nums[index])
#     sum1 = total + nums[index]
#     backtrack(index+1, sum1, subset)

#     subset.pop()
#     sum1 = total
#     backtrack(index+1,sum1, subset)

# nums = [1,2,3,4,5,6,7,8,9]
# result = []
# k = 4
# n = 13
# backtrack(0, 0,[])
# print(result)


# Optimal Solution
nums = [1,2,3,4,5,6,7,8,9]
result = []
k = 2
n = 8

def backtrack(last, total, subset):
    print("backtrack")
    if total == n and len(subset) == k:
        result.append(subset.copy())
        return

    if total > n and len(subset) > k:
        return

    for i in range(last,len(nums)):
        sum = total + i
        subset.append(i)
        print(sum, subset)
        backtrack(i+1, sum, subset)
        subset.pop()


backtrack(1, 0, [])
print(result)