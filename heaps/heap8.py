"""
Min heap sort
"""

def heapifyDownMin(arr, n, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != index:
        arr[smallest], arr[index] = arr[index], arr[smallest]
        heapifyDownMin(arr, n, smallest)

def heap_sort_descending(arr):
    n = len(arr)

    # Step 1: Build Min Heap
    for i in range(n // 2 - 1, -1, -1):
        heapifyDownMin(arr, n, i)

    # Step 2: Extract min one by one
    for last_index in range(n - 1, 0, -1):
        arr[0], arr[last_index] = arr[last_index], arr[0]
        heapifyDownMin(arr, last_index, 0)

    # Since we built a Min Heap, the array is now in ascending order.
    # We reverse it to get descending order.
    arr.reverse()
    return arr

import random

a = random.sample(range(1, 100), 8)
print("Original:", a)
sorted_desc = heap_sort_descending(a)
print("Sorted (Descending):", sorted_desc)
