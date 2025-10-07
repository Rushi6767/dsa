"""
Implementation of Queue
"""

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return "cannot dequeue, Queue is empty"
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            return "cannot front, Queue is empty"
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            return "cannot rear, Queue is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
# Instantiate the queue
queue = Queue()

# Check if queue is empty
print("Is empty?", queue.is_empty())  # True

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Check size
print("Size:", queue.size())  # 3

# Check front and rear
print("Front:", queue.front())  # 10
print("Rear:", queue.rear())    # 30

# Dequeue one element
print("Dequeued:", queue.dequeue())  # 10

# Check front and rear again
print("Front:", queue.front())  # 20
print("Rear:", queue.rear())    # 30

"""
is_empty, enqueue, front, rear, size
Time complexity: O(1)

for dequeue
Time complexity: O(n)

Space complexity: O(n)
"""