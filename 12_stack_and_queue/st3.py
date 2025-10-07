"""
Implement stack using Queue

Note
push(x): step1: append element
step2: rotate element n- 1 times

pop():remove 1st element
"""
from collections import deque

class Queue:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        for i in range(len(self.items) - 1):
            self.items.append(self.items.popleft())
        
    def pop(self):
        if len(self.items) == 0:
            return "Empty"
        x = self.items.popleft()
        return x

    def top(self):
        if len(self.items) == 0:
            return "Empty"
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
# Instantiate the queue
queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
# print(queue.top())
queue.push(40)

print(queue.size())
print(queue.top())
print(queue.pop())
print(queue.size())
print(queue.top())

"""
push
Time complexity:  O(n)
Space complexity: O(n)

for all oprerations pop, top(peek), size

Time complexity: O(1)
Space complexity: O(n)
"""