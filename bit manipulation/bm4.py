"""
set the ith bit
"""
def set_bit(n,i):
    result = n | (1 << i)
    print(result)

n = 9
i = 2
set_bit(n,i)

"""
Time complexity: O(1)
"""