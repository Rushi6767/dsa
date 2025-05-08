def subsets(nums, index=0, path=[]):
    if index == len(nums):
        print(path)
        return

    # Exclude current
    subsets(nums, index + 1, path)
    # Include current
    subsets(nums, index + 1, path + [nums[index]])

subsets([1, 2])
