"""
Implement Stack using Array/List
"""

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(5)
stack.push(6)
stack.push(7)
print(f"stack content = {stack}")
print(f"poped item  = {stack.pop()}")
print(f"stack content = {stack}")
print(f"stack is empty = {stack.is_empty()}")

"""
for all oprerations is_empty, push, pop, top, size

Time complexity: O(1)
Space complexity: O(n)
"""