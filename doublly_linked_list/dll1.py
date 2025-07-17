"""
Doublly Linked List methods
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        # Tc = O(1)
        # Sc = O(1)

    def append(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next 
            current.next = new_node
            new_node.prev = current

            # TC : O(n)
            # SC : O(n)
            
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        
        current = self.head
        count = 0
        while current and count<position-1:
            current = current.next
            count += 1

        if current is None:
            print("Position Out of Bound")
            return
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

        # Tc : O(n)
        # sc : O(1)

    def traverse(self):
        if self.head == None:
            print("Empty Doublly Linked List")
            return
        
        current = self.head
        while current:
            # print(current.val)
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next


    def delete_head(self):
        if self.head == None:
            print("Empty Doublly Linked List")
            return
        
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head == None:
            print("Empty Doublly Linked List")
            return
        
        if self.head.next is None:
            # Only one node in the list
            self.head = None
            return
        
        current = self.head
        while current.next:
            current = current.next
        print(current.val)

        current.prev.next = None
        current.prev = None



dll = DoublyLinkedList()
dll.traverse()
dll.insert_at_head(30)
dll.insert_at_head(20)
dll.append(40)
dll.insert_at(25, 2)
dll.traverse()
# dll.delete_head()
# dll.traverse()
dll.delete_end()
dll.traverse()