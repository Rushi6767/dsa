"""
Binary Tree Implementation
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

drink =Node("drink")
hot=Node("hot")
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanta=Node("fanta")

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

drink.left = hot
drink.right = cold

print(drink)
print(drink.val)
print(drink.left)
print(hot)
print(hot.val)
print(drink.left.left.val)
print(drink.right.val)
print(drink.right.right.val)