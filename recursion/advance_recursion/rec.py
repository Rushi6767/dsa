"""
find all subsequences

"""
def func(index, sub_set):
    if index >= len(nums):
        result.append(sub_set.copy())
        return
    sub_set.append(nums[index])
    func(index+1, sub_set)
    sub_set.pop()
    func(index+1, sub_set)

nums = [5,4,9]
result = []
func(0, [])

print(result)