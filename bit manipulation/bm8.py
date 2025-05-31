"""
Check if the number is power of 2
"""

n = 16

result = n & (n-1)
if result == 0:
    print("n is power of 2")
else:
    print("n is not power of 2")

"""
Time complexity: O(1)
Space complexity: O(1)
"""