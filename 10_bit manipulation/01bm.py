"""
convert int(decimal) to binary
"""

def convert2binary(num):
    result = ""

    while num > 0:
        if num%2 == 1:
            result += "1"
        else:
            result += "0"

        num = num//2

    result = result[::-1]
    return result

convert2binary(13)

"""
Time complexity: O(log2(n))
Space complexity: O(log2(n))
"""