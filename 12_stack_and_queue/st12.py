"""
3. Longest Substring Without Repeating Characters
"""
# s = "CADBZABCD"
# n = len(s)
# maxi = 0

# for i in range(n):
#     my_set = set()
#     for j in range(i, n):
#         if s[j] in my_set:
#             break
#         maxi = max(maxi, j-i+1)
#         my_set.add(s[j])
# print(maxi)

"""
Time complexity: O(n(n+1)/2) == O(n^2)
Space complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left = 0
        right = 0
        maxi = 0
        n = len(s)

        while right < n:
            if s[right] in d:
                left = max(left, d[s[right]]+1)

            maxi = max(maxi, right-left+1)
            d[s[right]] = right
            right += 1

        return maxi
    
s1 = Solution()
s = "CADBZABCD"
print(s1.lengthOfLongestSubstring(s))

"""
Time complexity: O(n)
Space complexity: O(n)
"""