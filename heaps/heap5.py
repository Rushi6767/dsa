"""
Build Min heap form given arry
"""

def heapifyDown(arr, index):
        n = len(arr)
        smallerid = index
        leftchildInd = 2 * index + 1
        rightchildIndex =  2 * index +2

        if leftchildInd < n and arr[leftchildInd] < arr[smallerid]:
            smallerid = leftchildInd

        if rightchildIndex < n and arr[rightchildIndex] < arr[smallerid]:
            smallerid = rightchildIndex

        if smallerid != index:
            arr[smallerid], arr[index] = arr[index], arr[smallerid]
            heapifyDown(arr, smallerid)

def BuildMinHeap(arry):
    n = len(arry)
    internal = n//2 - 1

    for i in range(internal, -1, -1):
        heapifyDown(arry, i)

    return arry


a = [1,8,7,16,11,12,2,4]
print(BuildMinHeap(a))


"""
Time complexity: sum (2^h) x logn-h == O(n)
Space complexity: O(1)
"""