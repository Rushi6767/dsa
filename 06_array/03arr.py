"""
check array is sorted or not
"""

def check(nums):
    for i in range(len(nums) -1):
        if nums[i] > nums[i+1]:
            return False
    return True

nums = [1,2,3,4,7,8,6]
print(check(nums))

"""
Time complexity : O(n)
Space complexity : O(1)
"""