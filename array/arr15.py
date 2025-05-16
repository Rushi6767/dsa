"""
128. Longest Consecutive Sequence
"""
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
# n = len(nums)
# max_count = 0

# # O(n)
# for i in range(n):
#     num = nums[i]
#     count = 1

#     # O(n)
#     while num +1 in nums:
#         count += 1
#         num += 1

#     max_count = max(max_count, count)
# print(max_count)


"""
Time complexity: O(n^2)
Space complexity: O(1)
"""


# # ======Better==============
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
# n = len(nums)
# # O(nlogn)
# nums[:] = sorted(nums)

# last_smaller = float("-inf")
# count = 0
# longest = 0

# # O(n)
# for i in range(n):
#     num = nums[i]

#     if num-1 == last_smaller:
#         count+=1
#         last_smaller = num

#     elif num != last_smaller:
#         count=1
#         last_smaller = num

#     longest = max(longest, count)

# print(longest)

"""
Time complexity: O(nlogn + n)
Space complexity: O(1)
"""


# =====================optimal=========
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
n = len(nums)
my_set = set()

for i in range(n):
    my_set.add(nums[i])

longest = 0

for num in my_set:
    if num-1 not in my_set:
        x = num
        count = 1

        while x+1 in my_set:
            count+=1
            x+=1

        longest = max(longest, count)

print(longest)

"""
Time complexity: O(n + n + n) === O(3n) ===== O(n)
Space complexity: O(n)
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set()

        for i in range(n):
            my_set.add(nums[i])

        longest = 0

        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1

                while x+1 in my_set:
                    count+=1
                    x+=1

                longest = max(longest, count)

        return longest