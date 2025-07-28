"""
simple question
i did because variasion of questions
simple apply max heap logic which did in heap4.py (same)

Convert min heap to max heap
"""

def heapifyDown(arr, index):
        n = len(arr)
        largeind = index
        leftchildInd = 2 * index + 1
        rightchildIndex =  2 * index +2

        if leftchildInd < n and arr[leftchildInd] > arr[largeind]:
            largeind = leftchildInd

        if rightchildIndex < n and arr[rightchildIndex] > arr[largeind]:
            largeind = rightchildIndex

        if largeind != index:
            arr[largeind], arr[index] = arr[index], arr[largeind]
            heapifyDown(arr, largeind)

def BuildMaxHeap(arry):
    n = len(arry)
    internal = n//2 - 1

    for i in range(internal, -1, -1):
        heapifyDown(arry, i)

    return arry


a = [2,4,7,6,10,9,11,9]
print(BuildMaxHeap(a))


"""
Time complexity: sum (2^h) x logn-h == O(n)
Space complexity: O(1)
"""