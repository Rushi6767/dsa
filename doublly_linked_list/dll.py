"""
How to create a node
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

n1 = Node(5)
n2 = Node(6)
n3 = Node(7)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
