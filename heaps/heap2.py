"""
Maximum Heap
"""

class MaximumHeap:
    def __init__(self):
        self.arr = []
        self.count = 0

    # TC : O(log n)
    def heapifyUp(self, index):
        parentInd = (index - 1)//2

        if index > 0 and self.arr[index] > self.arr[parentInd]:
            self.arr[index], self.arr[parentInd] = self.arr[parentInd], self.arr[index]
            self.heapifyUp(parentInd)

    # TC : O(log n)
    def heapifyDown(self, index):
        n = len(self.arr)
        largeind = index
        leftchildInd = 2 * index + 1
        rightchildIndex =  2 * index +2

        if leftchildInd < n and self.arr[leftchildInd] > self.arr[largeind]:
            largeind = leftchildInd

        if rightchildIndex < n and self.arr[rightchildIndex] > self.arr[largeind]:
            largeind = rightchildIndex

        if largeind != index:
            self.arr[largeind], self.arr[index] = self.arr[index], self.arr[largeind]
            self.heapifyDown(largeind)

    # TC : O(1)
    def inializeHeap(self):
        self.arr.clear()
        self.count = 0

    # TC : O(log n)
    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.count)
        self.count += 1

    # TC : O(log n)
    def changeKey(self, index, new_val):
        if new_val < self.arr[index]:
            self.arr[index] = new_val
            self.heapifyDown(index)
        else:
            self.arr[index] = new_val
            self.heapifyUp(index)

    # TC : O(log n)
    def extract_max(self):
        if self.count ==0:
            return None
        
        n = self.count
        ele = self.arr[0]
        self.arr[0], self.arr[n-1] = self.arr[n-1], self.arr[0]
        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapifyDown(0)
        return ele
    
    # TC : O(1)
    def isEmpty(self):
        return self.count == 0
    
    # TC : O(1)
    def getMax(self):
        return self.arr[0] if self.count > 0 else None
    
    # TC : O(1)
    def heapSize(self):
        return self.count
    

h = MaximumHeap()
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(1)

print(h.extract_max())  # ➜ 15
print(h.extract_max())  # ➜ 10
print(h.extract_max())  # ➜ 4
print(h.extract_max())  # ➜ 1
print(h.extract_max())  # ➜ None (heap is empty)
