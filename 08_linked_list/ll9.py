"""
19. Remove Nth Node From End of List
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
  

    def remove(self, p):
        temp = self.head
        n = 0

        while temp:
            n+=1
            temp = temp.next
        p = (n - p)

        a = 0
        prev = None
        t = self.head

        if p != 0:
            while p != a:
                a += 1
                prev = t
                t = t.next
            prev.next = t.next

        else:
            self.head = t.next
            self.next = None

        return self.head

    # same logic just show 
    def removeNthFromEnd(self):
        if head is None:
            return None


        length = 0
        current_node = head


        # Calculate the length of the linked list
        while current_node is not None:
            length += 1
            current_node = current_node.next


        # If the node to remove is the head of the list
        if length == n:
            new_head = head.next
            head = None
            return new_head


        # Find the node just before the one we want to remove
        position_to_stop = length - n
        current_node = head


        while current_node is not None:
            position_to_stop -= 1
            if position_to_stop == 0:
                break
            current_node = current_node.next


        # Remove the nth node from the end
        current_node.next = current_node.next.next
        return head
    """
    Time complexity: O[(n) + (n)] == O(2n) == O(n)
    Space complexity: O(1)
    """

    def removeNthFromEnd(self, n):
        slow = self.head
        fast = self.head

        for _ in range(n):
            fast = fast.next

        if fast == None:
            self.head = self.head.next
            return self.head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return self.head

    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

sll = SinglyLinkedList()
sll.append(1)
sll.append(3)
sll.append(4)
sll.append(7)
sll.append(1)
sll.append(2)
sll.append(6)
sll.traverse()            # 5 10 15
# sll.remove(2)
sll.removeNthFromEnd(2)
sll.traverse()