"""
45. Jump Game II
"""
nums = [2,3,0,1,4]
jump = 0
left =0
right =0
n = len(nums)

while right < n-1:
    far = 0
    for i in range(left,right+1):
        far = max(far, i+nums[i])
    left = right + 1
    right = far
    jump+=1

print(jump)

"""
Time complexity : O(n)
Space complexity : O(1)
"""