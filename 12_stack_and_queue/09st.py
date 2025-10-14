"""
155. min stack
"""

class Stack:

    def __init__(self):
        self.items = []
        self.minimum = float("-inf")

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, val):
        if len(self.items) == 0:
            self.items.append([val,val])
        else:
            mini = min(self.items[-1][1], val)
            self.items.append([val,mini])

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1][0]
    
    def size(self):
        return len(self.items)
    
    def get_min(self):
        if len(self.items) == 0:
            return 0
        return self.items[-1][1]
    
stack = Stack()
print(stack.get_min())
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min())
stack.pop()
print(stack.top())
print(stack.get_min())

"""
Time complexity :O(1)
Space complexity :O(n)
"""