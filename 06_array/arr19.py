"""
15. 3Sum
"""
# nums = [-1,0,1,2,-1,-4]
# n = len(nums)
# # print(nums)
# result = []

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if nums[i] + nums[j] + nums[k] == 0:
#                if sorted([nums[i], nums[j], nums[k]]) not in result:
#                     result.append(sorted([nums[i], nums[j], nums[k]]) )

# print(result)

"""
Time complexity : O(n^3)
Space complexity : O(k) where k is the number of unique triplets 
"""

# nums = [-1,0,1,2,-1,-4]
# n = len(nums)
# result_set = set()

# for i in range(n):
#     my_set = set()
#     for j in range(i+1, n):
#         third = -(nums[i] + nums[j])
#         if third in my_set:
#             temp = [nums[i], nums[j], third]
#             temp.sort()
#             result_set.add(tuple(temp))
#         my_set.add(nums[j])

# l1 = [list(ans) for ans in result_set]
# print(l1)

"""
Time complexity : O(n^2)
Space complexity : O(n)
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # moving the 2 pointers
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    # skip the duplicates if occurred
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans