"""
Implement Queue using 2 stack

push(x) here enqueue(x):
step 1:Transfer all element from stack 1 to stack 2
step 2:Insert element to stack1
step 3:Transfer all element from stack 2 to stack 1

pop() here dequeue(): pop top element of stack 1

peek(): return top element of stack 1
"""

class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,item):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(item)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if len(self.stack1) == 0:
            return "empty"
        x = self.stack1.pop()
        return x
    
    def peek(self):
        if len(self.stack1) == 0:
            return "empty"
        return self.stack1[-1]
    
    def size(self):
        return len(self.stack1)

s = StackQueue()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.size())
print(s.peek())
print(s.pop())
print(s.size())
print(s.peek())

"""
push
Time complexity: O(n) + O(1) + O(n) == O(2n) == O(n)
Space complexity: O(n)

for all oprerations pop, top(peek), size

Time complexity: O(1)
Space complexity: O(1)
"""