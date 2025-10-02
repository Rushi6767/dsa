"""
Generate all Binary strings
"""

def solve(index, flag, numbers):
    if index == n:
        result.append("".join(numbers))
        return
    numbers[index] = "0"
    solve(index+1, True, numbers)
    if flag == True:
        numbers[index] = "1"
        solve(index+1, False, numbers)
        numbers[index] = "0"

n = 3
numbers = [0] *n
result = []
# print(numbers)
solve(0, True, numbers)
print(result)