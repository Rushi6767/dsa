"""
Find the lenth of loop
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

    
    def lenght_of_loop(self):
        temp = self.head
        d = {}
        travel = 0

        while temp:
            if temp in d:
                return travel - d[temp]
            d[temp] = travel
            travel+=1
            temp = temp.next

    """
    time complexity: O(n)
    space complexity: O(n)
    """

    def find_cycle(self):
        slow = self.head
        fast= self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = slow.next
                count = 1

                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        else: return 0

    """
    time complexity: O(n)
    space complexity: O(1)
    """


sll = SinglyLinkedList()
sll.traverse()            # Empty
sll.append(5)
sll.append(10)
sll.append(15)
sll.traverse()            # 5 10 15