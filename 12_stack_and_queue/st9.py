"""
monotonic stack

Next Greater Element
"""
# nums = [19, 4, 2, 11, 6, 5, 3, 10]
# n = len(nums)
# result = []

# for i in range(n):
#     result.append(-1)
#     for j in range(i+1, n):
#         if nums[i]<nums[j]:
#             result.pop()
#             result.append(nums[j])
#             break

# print(result)

# nums = [19, 4, 2, 11, 6, 5, 3, 10]
# n = len(nums)
# result = [-1] * n

# for i in range(n):
#     for j in range(i+1, n):
#         if nums[i]<nums[j]:
#             result[i] = nums[j]
#             break

# print(result)

"""
Time complexity O(n(n+1)/2) == O(n^2)
Space complexity == O(1) or O(n)but return
"""

# =====optimal======
"""
Monotonic stack: same but stored in order(ascendic or descendic)
"""
nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)
result = [-1] * n
stack = []

for i in range(n-1, -1, -1):
    while len(stack) != 0 and stack[-1] <= nums[i]:
        stack.pop()
    if len(stack) != 0:
        result[i] = stack[-1]
    stack.append(nums[i])

print(result)

"""
Time complexity O(2n)
Space complexity == O(n)
"""