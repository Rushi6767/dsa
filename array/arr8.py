"""
Merge 2 sorted array
"""

# nums1 = [1,1,1,2,4,6,7]
# nums2 = [1,2,3,6,7,8,9,10]
# d = {}
# for i in nums1:
#     d[i] = 0

# for j in nums2:
#     d[j] = 0

# print(sorted(list(d)))

"""
Time complexity: O((n + m)log(n + m))
Space complexity: O(n + m)
"""


nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]
i = 0
j = 0
result = []

while i < len(nums1) and j<len(nums2):
    # if result != []:
        
    if nums1[i] <= nums2[j]:
        if result != [] and result[-1] == nums1[i]:
            i+=1
        else:
            result.append(nums1[i])
            i+=1
    else:
        if result != [] and result[-1] == nums2[j]:
            j+=1
        else:
            result.append(nums2[j])
            j+=1

if i < len(nums1):
    while i < len(nums1):
        if result[-1] == nums1[i]:
            i+=1
        else:
            result.append(nums1[i])
            i+=1

if j < len(nums2):
    while j < len(nums2):
        if result[-1] == nums2[j]:
            j+=1
        else:
            result.append(nums2[j])
            j+=1


print(result)

"""
Time complexity: O(n+m)
Space complexity: O(1)
if we count memory or worst case or interviewer ask : O(n+m)
"""