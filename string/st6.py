"""
Frequency map/ dictionary
store frequency in dictinary
"""

# nums =[5,6,7,7,1,9,1,1,5,1,1]
# d = {}

# for i in nums:
#     d[i]=nums.count(i)

# print(d)

# nums =[5,6,7,7,1,9,1,1,5,1,1, 8]
# d = {}
# c = 1
# for i in nums:
#     if i not in d:
#         d[i]=c
#     else:
#         d[i] = c +1

# print(d)

# nums =[5,6,7,7,1,9,1,1,5,1,1,8]
# d = {}

# for i in nums:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i] += 1

# print(d)


"""
Time complexity: O(n)
Space complexity: O(n)
"""
nums =[5,6,7,7,1,9,1,1,5,1,1,8]
d = {}

for i in nums:
    d[i] = d.get(i, 0) + 1
print(d)

# nums =[5,6,7,7,1,9,1,1,5,1,1,8]
# d = {}

# for i in range(0, len(nums)):
#     d[nums[i]] = d.get(nums[i], 0) + 1
# print(d)

