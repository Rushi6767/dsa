"""
Delete all occurrences of a given key in a doubly linked list
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

    def deleteAllOccurOfX(self, head, k):
        # Handle special case: single node that matches the key
        if not head.next and head.data == k:
            return None
        
        temp = head          # Pointer to traverse the list
        previous = None      # Pointer to track previous node
        new_head = head      # Keep track of new head
        
        # Traverse through the entire list
        while temp is not None:
            if temp.data == k:  # Found a node to delete
                # Update previous node's next pointer
                if previous:
                    previous.next = temp.next
                
                # Update next node's prev pointer
                if temp.next:
                    temp.next.prev = previous
                
                # Update head if we're deleting the first node
                if temp == new_head:
                    new_head = new_head.next
            
            previous = temp      # Move previous pointer
            temp = temp.next     # Move to next node
        
        return new_head
    
    # TC : O(n)
    # SC : O(1)




dll = DoublyLinkedList()
dll.insert_at_head(20)
dll.insert_at_head(2)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(10)
dll.traverse()
dll.deleteAllOccurOfX(2)
dll.traverse()
