"""
Remove duplicate from array (in place)
"""
# nums = [1,1,1,2,3,4,4,7,9,9,9,10]
# n = len(nums)
# d ={}

# for i in nums:
#     d[i] = 0
# j = 0
# for k in d:
#     nums[j] = k
#     j+=1

# print(nums)

"""
Time complexity : O(2n) == O(n)
Space complexity : O(n)
"""

def remove_duplicates(nums):
    n = len(nums)
    i = 0
    j = i+1
    if n==1:
        return 1
    
    while j < n:
        if nums[j] != nums[i]:
            i+=1
            nums[j], nums[i] = nums[i], nums[j]
        j+=1
    return i+1

nums = [1,1,1,2,3,4,4,7,9,9,9,10]
print(remove_duplicates(nums))

"""
Time complexity : O(n)
Space complexity : O(1)
"""