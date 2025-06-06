"""
min stack
"""

class Stack:

    def __init__(self):
        self.items = []
        self.minimum = float("-inf")

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if self.items == []:
            self.minimum = item
        else:
            self.minimum = min(self.minimum, item)
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        # self.minimum = min(self.minimum, item)
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def get_min(self):
        return self.minimum
    
stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(1)
stack.push(10)
print(stack.get_min())
stack.pop()
stack.pop()
print(stack.get_min())

