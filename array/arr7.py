"""
Linear search
"""
def lin_search(nums, t):
    for i in range(len(nums)):        
        if nums[i] == target:
            return i
    return -1
   
nums= [5,4,3,9,8,1,6,-10,-100]
target = 4
print(lin_search(nums, target))

"""
Time complexity : O(n)
Space complexity : O(1)
"""
