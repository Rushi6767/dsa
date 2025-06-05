"""
Implementing Stack using Doubly linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class StackDLL:
    def __init__(self):
        self.head = None  # bottom of stack
        self.tail = None  # top of stack
        self.count = 0

    def push(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def pop(self):
        if self.tail is None:
            return "Empty"
        data = self.tail.data
        if self.head == self.tail:  # only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return data

    def top(self):
        if self.tail is None:
            return "Empty"
        return self.tail.data

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

stack = StackDLL()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())     # 30
print(stack.pop())     # 30
print(stack.size())    # 2
print(stack.top())     # 20
print(stack.is_empty())  # False

"""
For all operations
Time complexity: O(1)
Space complexity: O(1)
"""