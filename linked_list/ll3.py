"""
876. Middle of the Linked List
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

    def middle(self):
        count = 0
        if not self.head:
            print("Empty")
        else:
            current = self.head
            while current:
                # print(current.val)
                count+=1
                current = current.next
        print(count)
        c = count//2
        c2 = 0
        current = self.head
        while current:
            if c2>= c:
                print(current.val)
            c2 += 1
            current = current.next

    def middle_brute(self):
        temp = self.head
        count = 0
        if not self.head:
            print("Empty")
        else:
            current = self.head
            while current:
                count+=1
                current = current.next
        
        current = self.head
        for i in range(count//2):
            current = current.next
        return current
    """
    Time complexity: O(n + (n/2))
    Space complexity: O(1)
    """

    def middleNode(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    """
    Time complexity: O(n/2)
    Space complexity: O(1)
    """

        

sll = SinglyLinkedList()
# sll.traverse()            # Empty
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.traverse()            # 5 10 15
print(sll.middleNode().val)

# sll.middle()
# middle_node = sll.middle_brute()
# if middle_node:
#     print("Middle value:", middle_node.val)

