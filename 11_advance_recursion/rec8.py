"""
subset sum 1
"""


# def backtrac(index, subset):
#     if index >= len(nums):
#         result.append(sum(subset.copy()))
#         return
#     subset.append(nums[index])
#     backtrac(index+1, subset)
    
#     subset.pop()
#     backtrac(index+1, subset)

# nums = [5,9,3]
# result = []
# backtrac(0, [])
# print(result)




def backtrac(index, total):
    if index >= len(nums):
        result.append(total)
        return
    sum1 = total + nums[index]
    backtrac(index+1, sum1)
    
    sum1 = total
    backtrac(index+1,sum1)

nums = [5,9,3]
result = []
backtrac(0,0)
print(result)