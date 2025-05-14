"""
485 Max consecutive ones
"""
# nums = [1,1,0,1,0,1,1,1,1,0,1,1]
# result = []
# val = 0

# for i in nums:
#     if i == 1:
#         val+=1
#     else:
#         result.append(val)
#         val = 0
# result.append(val)

# print(max(result))
"""
Time complexity: O(n)
Space complexity: O(1)
"""

nums = [1,1,0,1,0,1,1,1,1,0,1,1]
# nums = [1,1,0,1,1,1]
val = 0
m = 0

for i in nums:
    if i == 1:
        val+=1
    else:
        m = max(val, m)
        val = 0
m = max(val, m)
print(m)
"""
Time complexity: O(n)
Space complexity: O(1)
"""