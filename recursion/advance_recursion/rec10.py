"""
Letter Combination of Phone number
"""
result = []
d = {"2":"abc", "3":"def", "4": "ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}
digit = "23"

def backtrack(index, subset):
    print(index, subset)
    if index >= len(digit):
        result.append(subset.copy())
        return

    for i in d[digit[index]]:
        subset.append(i)
        backtrack(index+1,subset )
        subset.pop()
    

backtrack(0, [])
print(result)