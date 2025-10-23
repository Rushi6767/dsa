"""
we are solve sliding window problems
Next Greater Element II
"""

nums = [19, 4, 2, 11, 6, 5, 3, 10]
n = len(nums)
r = 2 * (n-1)
result = [-1] * n
stack = []

for i in range(r, -1, -1):
    while len(stack) != 0 and stack[-1] <= nums[i%n]:
        stack.pop()
    if i < n:
        if len(stack) != 0:
            result[i] = stack[-1]
    stack.append(nums[i % n])

print(result)

"""
Time complexity O(2 x 2n)
Space complexity == O(n)
"""