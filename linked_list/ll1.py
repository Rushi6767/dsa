"""
Singly Linked list (travel in one direction)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("Single linked list is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count +=1
            prev_node.next = new_node
            new_node.next = current

    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val ==val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not Found")

sll = SinglyLinkedList()
sll.traverse()            # Empty
sll.append(5)
sll.append(10)
sll.append(15)
sll.traverse()            # 5 10 15
sll.insert_at(7, 1)
sll.traverse()            # 5 7 10 15
sll.delete(10)
sll.traverse()            # 5 7 15
sll.delete(5)
sll.traverse()            # 7 15
sll.delete(100)           # Node not Found
