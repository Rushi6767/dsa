"""
Sort
step1: convert in maxheap
step2: use extract max
swap first and last element
heapify down
"""

import random

def heapifyDown(arr, n, index):
    largeind = index
    leftchildInd = 2 * index + 1
    rightchildIndex =  2 * index +2

    if leftchildInd < n and arr[leftchildInd] > arr[largeind]:
        largeind = leftchildInd

    if rightchildIndex < n and arr[rightchildIndex] > arr[largeind]:
        largeind = rightchildIndex

    if largeind != index:
        arr[largeind], arr[index] = arr[index], arr[largeind]
        heapifyDown(arr, n, largeind)

def heap_sort(arr):
    n = len(arr)

    # Build Max Heap Tc :O (N)
    for i in range(n//2-1, -1, -1):
        heapifyDown(arr, n, i)

    # Extract element from heap one by one Tc :O (N x logN)
    for last_index in range(n-1, 0, -1):
        arr[0], arr[last_index] = arr[last_index], arr[0]
        heapifyDown(arr, last_index, 0)

    return arr

a = random.sample(range(1, 100), 8)
print(f"arry {a}")

sorted = heap_sort(a)
print("Sorted :", sorted)
"""
Time complexity: O( N + (N x logN))
Space complexity: O(1)
"""