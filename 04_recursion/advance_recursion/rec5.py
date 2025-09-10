"""
Generate Parenthesis
"""
def backtrack(index, total, subset):
    print(index, total, subset)
    if index >= len(subset) :
        print(subset)
        if total==0:
            result.append("".join(subset.copy()))
        return
    if total > len(subset)//2:
        return
    if total < 0:
        return

    subset[index] = "("
    sum1 = total + 1 
    backtrack(index+1, sum1, subset)

    subset[index] = ")"
    sum1 = total - 1
    backtrack(index+1, sum1, subset)



num = 2
nums = [""] * (num*2)
result = []
backtrack(0,0, nums)
print(result)