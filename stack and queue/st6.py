"""
Implementing Queue using Double linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class QueueDll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        new_node = Node(item)

        if self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1
        
    def dequeue(self):
        if self.tail is None:
            return "Empty"
        x = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return x
    
    def front(self):
        if self.tail is None:
            return "Empty"
        else:
            return self.head.data
        
    def rear(self):
        if self.tail is None:
            return "Empty"
        else:
            return self.tail.data
        
    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count
    
qd = QueueDll()
qd.enqueue(10)
qd.enqueue(20)
qd.enqueue(30)

print(qd.front())   # 10
print(qd.rear())    # 30

qd.dequeue()

print(qd.front())   # 20
print(qd.rear())    # 30
print(qd.size())    # 2
print(qd.is_empty())  # False

"""
for all operations
Time complexity: O(1)
Space complexity: O(1)
"""