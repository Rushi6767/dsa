"""
convert binary to int(decimal)
"""

def convert2decimal(binary):
    decimal_num = 0
    power = 0
    index = len(binary) - 1

    while index >= 0:
        num = int(binary[index]) * (2 ** power)
        decimal_num += num

        power += 1
        index -= 1
    print(decimal_num)

convert2decimal('1101')

"""
Time complexity: O(len)
Space complexity: O(1)
"""