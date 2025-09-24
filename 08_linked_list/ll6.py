"""
142. Linked List Cycle II
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

    def cycle(self):
        temp = self.head
        s = set()

        while temp:
            if temp in s:
                return temp
            s.add(temp)
            temp = temp.next
        return -1
    """
    time complexity: O(n)
    space complexity: O(n)
    """

    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = self.head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    # diff style same code, logic same
    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None
        
        slow = self.head

        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    """
    time complexity: O(n)
    space complexity: O(1)
    """

sll = SinglyLinkedList()
sll.append(5)
sll.append(10)
sll.append(15)
sll.traverse()            # 5 10 15
print(sll.cycle())