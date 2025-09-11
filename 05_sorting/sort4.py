"""
4.merge sort
"""
print('merge two sorted array')

def merge_arry(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    if i < len(left):
        while i < len(left):
            result.append(left[i])
            i+=1
    if j < len(right):
        while j < len(right):
            result.append(right[j])
            j+=1
    return result

# left = [1,2,3,4]
# right = [1,1,3,4,5,6,7]
# print(merge_arry(left, right))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_arry(left_half, right_half)

arr = [3,1,6,2,4,8,7]
print(merge_sort(arr))

"""
Time complexity: O(nlogn)
Space complexity: O(n)
"""