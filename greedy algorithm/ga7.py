"""
Minimum Platforms
"""

# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]
# n = len(arr)
# ans = 1
# for i in range(n):
#     count = 1
#     for j in range(i + 1, n):
#         if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (
#             arr[j] >= arr[i] and arr[j] <= dep[i]
#         ):
#             count += 1
#     ans = max(ans, count)

# print(ans)

# ===optimal===========

class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        # O(2 x nlogn)
        arr.sort()
        dep.sort()

        ans = 1
        count = 1
        i = 1
        j = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:  # one more platform needed
                count += 1
                i += 1
            else:  # one platform can be reduced
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(dep)
s = Solution()
print(s.minimumPlatform(n, arr, dep))

"""
Time complexity : O(2 x nlogn) + O(n+ n) == O(2(nlogn + n)) == O(nlogn+n)
Space complexity : O(1)
"""