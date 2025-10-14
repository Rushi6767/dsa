"""
1423. Maximum Points You Can Obtain from Cards
"""

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = 0
        right_sum = 0
        d = {}
        maxi = 0

        if n == k:
            return sum(cardPoints)

        for i in range(k):
            left_sum += cardPoints[i]

        maxi = left_sum
        right_index = n-1

        for i in range(k-1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_index]
            maxi = max(maxi, left_sum+right_sum)
            right_index -= 1

        return maxi

s= Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(s.maxScore(cardPoints, k))

"""
Time complexity : O(n) + O(n) == O(2n) ==O(n)
Space complexity : O(1)
"""