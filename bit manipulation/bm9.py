"""
2220. Minimum Bit Flips to Convert Number
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0

        for i in range(0,32):
            if ans & (1<<i) != 0:
                count += 1
        return count
    
start = 10
goal = 7
s = Solution()
# print(s.minBitFlips(start, goal))

"""
Time complexity: O(32)
Space complexity: O(1)
"""


def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0

        while ans > 0:
            if ans%2 == 1:
                count+=1
            ans = ans // 2
        return count

start = 10
goal = 7
print(s.minBitFlips(start, goal))



"""
Time complexity: O(log2(n))
Space complexity: O(1)
"""