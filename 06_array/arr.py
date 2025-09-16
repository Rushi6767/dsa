"""
Largest elememt in array
"""

# a = [55,32,-97,99,3,67]

# l = a[0]
# for i in a:
#     if l < i:
#         l = i

# print(l)


# a = [55,32,-97,99,3,67]
# l = a[0]

# for i in range(0, len(a)):
#     if l < a[i]:
#         l = a[i]

# print(l)

a = [55,32,-97,99,3,67]

l = a[0]
for i in a:
    l = max(l, i)

print(l)

"""
Time complexity : O(n)
Space complexity : O(1)
"""