"""
Remove duplicate from sorted dll
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
            

    def traverse(self):
        if self.head == None:
            print("Empty Doublly Linked List")
            return
        
        current = self.head
        while current:
            # print(current.val)
            print(current.val, end=" <-> " if current.next else "\n")
            current = current.next

    def remove_dup(self):
        temp = self.head
        prev = None

        while temp and temp.next:
            if temp.val == temp.next.val:
                duplicate = temp.next
                temp.next = duplicate.next 
                if duplicate.next:
                    duplicate.next.prev = temp
            else:
                temp = temp.next
    # Tc: O(n)
    # sc : O(1)


dll = DoublyLinkedList()
dll.insert_at_head(2)
dll.insert_at_head(2)
dll.append(2)
dll.append(6)
dll.append(6)
dll.append(9)
dll.append(9)
dll.traverse()
dll.remove_dup()
dll.traverse()

