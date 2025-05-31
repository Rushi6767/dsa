"""
check the ith bit is set or not
"""
# print(bin(13))
# 0b1101

# def brute_force(n, i):
#     # Convert to binary string and reverse it to index from right to left
#     b = bin(n)[2:][::-1]  # binary string without '0b', reversed
#     if i < len(b) and b[i] == '1':
#         return True
#     return False

# # Example
# n = 13  # binary: 1101
# i = 2 
# print(brute_force(n, i))
"""
Time complexity: O(log(n))
"""

# # by using left shift
# def check_with_left_shift(n, i):
#     if (n & (1<<i)) != 0:
#         return True
#     else:
#         return False
    
# n = 13
# i = 1
# print(check_with_left_shift(n, i))


# by using right shift
def check_with_right_shift(n, i):
    if ((n >> i) & 1) == 1:
        return True
    else:
        return False
    
n = 13
i = 2
print(check_with_right_shift(n, i))

"""
Time complexity: O(1)
"""