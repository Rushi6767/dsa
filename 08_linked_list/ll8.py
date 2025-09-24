"""
328. Odd Even Linked List
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

    def brute_Odd_even(self):
        if self.head is None and self.head.next is None:
            return head

        values = []
        odd = self.head
        even = self.head.next

        while odd and odd.next:
            values.append(odd.val)
            odd = odd.next.next

        if odd:  # catch last node if length is odd
            values.append(odd.val)

        while even and even.next:
            values.append(even.val)
            even = even.next.next
            
        if even:
            values.append(even.val)


        print(values)
        temp = self.head
        for i in values:
            temp.val = i
            temp = temp.next

    """
    Time complexity: O[(n/2) + (n/2) + (n) ] == O(2n) == O(n)
    Space complexity: O(n)
    """

    # same code below
    def test(self):
        if self.head is None and self.head.next is None:
            return head

        temp = self.head
        values = []

        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
         temp = head.next
        while temp:
            values.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break

        index = 0
        temp = head
        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next
        return head

    def oddEvenList(self):
        if not self.head or not self.head.next:
            return head

        odd = self.head
        even = self.head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head
        
    """
    Time complexity: O(n/2) == O(n)
    Space complexity: O(1)
    """

sll = SinglyLinkedList()
sll.append(8)
sll.append(7)
sll.append(1)
sll.append(5)
sll.append(6)
sll.append(4)
sll.append(9)
sll.traverse()
# sll.brute_Odd_even()
sll.test()
sll.traverse()