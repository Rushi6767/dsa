"""
451. Sort Characters By Frequency
"""
# variant 1
class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        d = {}
        res = ""
        # O(n)
        for i in range(n):
            d[s[i]] = d.get(s[i], 0) + 1

        # O(n logn)
        sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)

        # O(n) but i think# O(26)
        for ch, freq in sorted_d:
            res = res + (ch * freq)
        return res


s = "treea"
sol = Solution()
# print(sol.frequencySort(s))

"""
Time Complexity : O(n + nlog(n) + n) == O(nlog(n) + 2n) == O(n logn) + O(n)
Space Complexity : O(n + k) where k English letters, k ≤ 26
"""


# variant 2 sort with coording the ascii
class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        d = {}
        res = ""
        # O(n)
        for i in range(n):
            d[s[i]] = d.get(s[i], 0) + 1

        # O(n logn)
        sorted_d = sorted(d.items(), key=lambda x:(-x[1], x[0]))

        # O(n) but i think# O(26)
        for ch, freq in sorted_d:
            res = res + (ch * freq)
        return res


s = "aacacc"
sol = Solution()
print(sol.frequencySort(s))

"""
Time Complexity : O(n + nlog(n) + n) == O(nlog(n) + 2n) == O(n logn) + O(n)
Space Complexity : O(n + k) where k English letters, k ≤ 26
"""