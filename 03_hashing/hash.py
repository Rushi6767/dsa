"""
cont value
constain:
1 <= n[i] <= 10
"""

# m = [5,3,2,2,1,5,5,7,5,10]
# n = [10,11, 1,9,5,6,2]

# l = []

# for i in n:
#     if i in m:
#         l.append(m.count(i))
#     else:
#         l.append(0)

# print(l)

# # ==with hashing====================
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# # pre store and only go to 10
# l = [0] * 11

# for num in n:
#     l[num] +=1
# for num in m:
#     if num < 1 or num > 10:
#         print(0)
#     else:
#         print(l[num])

"""
Time complexity : O(n + m)
Space complexity : O(1)


if we use 2 loops
Time complexity : O(n x m)
Space complexity : O(1)
"""


# # ==with hashing and dictionary====================
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# # pre store and only go to 10
# l = [0] * 11
# d = {}
# c = 0

# for num in n:
#     if num not in d:
#         d[num] =  1
#     else:
#         d[num] = d[num] + 1
# for num in m:
#     if num < 1 or num > 10:
#         print(0)
#     elif num not in d:
#         print(0)
#     else:
#         print(d[num])


# =====question 2========================
# s = "azyuyyzaaaa"
# q = ["d","a","y","u"]

# d = {}
# for i in q:
#     if i in s:
#         print(s.count(i))
#     else:
#         print(0)


# s = "azyuyyzaaaa"
# q = ["d","a","y","u"]

# d = {}
# c = 0

# for i in s:
#     # if i not in d:
#     #     d[i] = 1
#     # else:
#     #     d[i] += 1 
#     d[i] = d.get(i, 0) + 1
# print(d)

# for i in q:
#     if i in d:
#         print(d[i])
#     else:
#         print(0)


# ===with list=========
s = "azyuyyzaaaa"
q = ["d","a","y","u"]
l = [0] *26

for i in s:
    asc = ord(i)
    index = asc - 97
    l[index] += 1
for i in q:
    ascii = ord(i)
    index = ascii - 97
    print(l[index])


"""
Time complexity : O(n + m)
Space complexity : O(26) == O(1)

"""