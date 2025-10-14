"""
904. Fruit Into Baskets
"""
# fruits = [1,2,3,2,2]
# n =len(fruits)
# maxi = 0

# for i in range(n):
#     my = set()
#     for j in range(i, n):
#         my.add(fruits[j])
#         if len(my) > 2:
#             break
        
#         maxi = max(maxi, j-i+1)

# print(maxi)

"""
Time complexity: O(n(n+1)/2) == O(n^2)
Space complexity: O(3) == O(1)
"""

# ====better==========
# fruits = [1,2,3,2,2]
# n =len(fruits)
# maxi = 0
# left =0
# right =0
# d = {}

# while right < n:
#     d[fruits[right]] = d.get(fruits[right], 0) + 1


#     while len(d)>2:
#         d[fruits[left]] -= 1
#         if d[fruits[left]] == 0:
#             del d[fruits[left]]
#         left+=1

#     maxi = max(maxi, right-left+1)
#     right += 1

# print(maxi)
# print(d)

# """
# Time complexity: O(n) + O(n) == O(2n)
# Space complexity: O(3) == O(1)
# """

# ====Optimal==========
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n =len(fruits)
        maxi = 0
        left =0
        right =0
        d = {}

        while right < n:
            d[fruits[right]] = d.get(fruits[right], 0) + 1

            if len(d)>2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left+=1

            if len(d) <= 2:
                maxi = max(maxi, right-left+1)
            right += 1

        return maxi
fruits = [1,2,3,2,2]
s = Solution()
print(s.totalFruit(fruits))

"""
Time complexity: O(n)
Space complexity: O(3) == O(1)
"""


        