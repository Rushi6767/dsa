"""
Minimum Heap
"""

class MinimumHeap:
    def __init__(self):
        self.arr = []
        self.count = 0

    # Remove the parameter and just use self.arr inside the method.
    # TC : O(log n)
    def heapifyUp(self, arr, index):
        parentInd = (index - 1)//2

        if index > 0 and arr[index] < arr[parentInd]:
            arr[index], arr[parentInd] = arr[parentInd], arr[index]
            self.heapifyUp(arr, parentInd)

    # Remove the parameter and just use self.arr inside the method.
    # TC : O(log n)
    def heapifyDown(self, arr, index):
        n = len(arr)
        smallestInd = index
        leftchildInd = 2 * index + 1
        rightchildIndex =  2 * index +2

        if leftchildInd < n and arr[leftchildInd] < arr[smallestInd]:
            smallestInd = leftchildInd

        if rightchildIndex < n and arr[rightchildIndex] < arr[smallestInd]:
            smallestInd = rightchildIndex

        if smallestInd != index:
            arr[smallestInd], arr[index] = arr[index], arr[smallestInd]
            self.heapifyDown(arr, smallestInd)

    # TC : O(1)
    def inializeHeap(self):
        self.arr.clear()
        self.count = 0

    # TC : O(log n)
    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.arr, self.count)
        self.count += 1

    # TC : O(log n)
    def changeKey(self, index, new_val):
        if new_val > self.arr[index]:
            self.arr[index] = new_val
            self.heapifyDown(self.arr, index)
        else:
            self.arr[index] = new_val
            self.heapifyUp(self.arr, index)

    # TC : O(log n)
    def extract_min(self):
        if self.count ==0:
            return None
        
        n = len(self.arr)
        ele = self.arr[0]
        self.arr[0], self.arr[n-1] = self.arr[n-1], self.arr[0]
        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapifyDown(self.arr, 0)
        return ele
    
    # TC : O(1)
    def isEmpty(self):
        return self.count == 0
    
    # TC : O(1)
    def getMin(self):
        return self.arr[0] if self.count > 0 else None
    
    # TC : O(1)
    def heapSize(self):
        return self.count
    

h = MinimumHeap()
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(1)

print(h.extract_min())  # 1
print(h.extract_min())  # 4
print(h.getMin())       # 10
