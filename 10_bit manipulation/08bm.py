"""
Remove the last set bit [Right Most]
"""

n = 16

result = n & (n-1)
print(result)

"""
Time complexity: O(1)
Space complexity: O(1)
"""