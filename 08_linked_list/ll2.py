
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # Empty Linked List
        self.head = None

        # nu of nodes in LL
        self.n = 0

    # magic methods
    def __len__(self):
        return self.n
    
    def insert_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    # def traverse(self):
    def __str__(self):
        curr = self.head
        result = ''

        while curr != None:
            result = result + str(curr.val) + "->"
            curr = curr.next
        return result[:-2]
    
    def append(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        
        curr = self.head 
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self,after,val):
        new_node = Node(val)

        curr = self.head
        while curr != None:
            if curr.val == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return "Item Not Found"
        
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty Linked List'
        
        self.head = self.head.next
        self.n = self.n -1

    def pop(self):
        if self.head == None:
            return "Empty Linked List"
        
        curr = self.head

        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n = self.n -1

    def remove(self, val):
        if self.head == None:
            return "Empty Linked List"
        
        if self.head.val == val:
            return self.delete_head()
        
        curr = self.head
        while curr.next != None:
            if curr.next.val == val:
                break
            curr = curr.next

        if curr.next == None:
            return "Not found"
        else:
            curr.next = curr.next.next

    def search(self,item):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.val == item:
                return pos
            curr = curr.next
            pos = pos +1

        return 'Not Found'
    
    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.val
            curr = curr.next
            pos = pos + 1
        return"IndexError"

l = LinkedList()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
# l.traverse()
print(l)
# print(len(l))
# l.append(9)
print(l)
# print(len(l))
l.insert_after(20,200)
print(l)