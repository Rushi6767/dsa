"""
206. Reverse Linked List
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

    def rev(self):
        if not self.head:
            return self.head
        else:
            temp = self.head
            while temp:
                self.head = temp
                temp = temp.next
        return self.head
    
    # not good solution
    def rev_brute(self):
        if not self.head:
            print("empty")
        else:
            temp = self.head
            stack = []

            while temp:
                stack.append(temp.val)
                temp = temp.next

            temp = self.head

            while temp:
                e = stack.pop()
                temp.val = e
                temp = temp.next

    """
    Time complexity: O(n + n) == O(n)
    Space complexity: O(n)
    """

    # always use this while reverse linked list
    def reverseList(self): 
        temp = self.head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
    
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
                
sll = SinglyLinkedList()
sll.append(5)
sll.append(10)
sll.append(15)
sll.traverse()            # 5 10 15
# print(sll.rev().val)

# sll.rev_brute()

# print("Reversed list (by value):")
# sll.traverse()  # 15 10 5

print(sll.reverseList().val)