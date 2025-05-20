"""
4 sum problem
"""

# nums = [1,0,-1,0,-2,2]
# target = 0
# n = len(nums)
# result = []

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             for l in range(k+1, n):
#                 if nums[i] + nums[j] + nums[k] + nums[l] == target:
#                     if sorted([nums[i] , nums[j] , nums[k] , nums[l]]) not in result:
#                         result.append(sorted([nums[i] , nums[j] , nums[k] , nums[l]]))

# print(result)

"""
Time complexity : O(n^4)
Space complexity : O(n)
"""

# nums = [1,0,-1,0,-2,2]
# target = 0
# n = len(nums)
# result_set = set()

# for i in range(n):
#     for j in range(i+1, n):
#         my_set = set()
#         for k in range(j+1, n):
#             fourth = target - (nums[i] + nums[j] + nums[k])

#             if fourth in my_set:
#                 temp = [nums[i], nums[j], nums[k], fourth]
#                 temp.sort()
#                 result_set.add(tuple(temp))

#             my_set.add(nums[k])

# print(result_set)

# result = [list(ans) for ans in result_set]
# print(result)

"""
Time complexity : O(n^3)
Space complexity : O(n)
"""

nums = [1,0,-1,0,-2,2]
target = 0
n = len(nums)
ans = []
# O(nlogn)
nums.sort()

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    for j in range(i+1, n):
        if j > i+1 and nums[j] == nums[j-1]:
            continue

        k = j+1
        l = n-1

        while k < l:
            total = nums[i] + nums[j] + nums[k] + nums[l]
            if total == target:
                ans.append([nums[i], nums[j], nums[k], nums[l]])
                k+=1
                l-=1

                while k < l and nums[k] == nums[k-1]:
                    k += 1
                while k < l and nums[l] == nums[l+1]:
                    l -= 1
            elif total < target:
                k+=1
            else:
                l-=1

print(ans)

"""
Time complexity : O(n^2 x n) == O(n^3)
O(nlogn) ignore because O(nlogn) < O(n^3)
O(nlogn) is too small than O(n^3)

Space complexity : O(nu of ans)
if ans ignore then; Space complexity : O(1)
"""