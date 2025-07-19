"""
find pairs with given sum
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

    def brut_find_t(self, target):
        if self.head == None:
            return "Empty"
        
        l = []
        result = []    
        current = self.head
        while current:
            if current.val < target + 1:
                l.append(current.val)
            current = current.next
        
        for i in range(len(l)):
            for j in range(i, len(l)):
                if l[i] + l[j] == target:
                    result.append([l[i], l[j]])

        print(result)

    def better_find_t(self, target):
        if self.head == None:
            return "Empty"
        
        l = []
        current = self.head
        while current:
            if current.val < target + 1:
                l.append(current.val)
            current = current.next        
        start = 0
        end = len(l) -1
        result = []
        while start < end:
            if l[start] + l[end] == target:
                result.append([l[start], l[end]])
            start += 1
            end -= 1

        return result
    
    def brut_findPairsWithGivenSum(self, target):
        result = []    
        temp1 = self.head
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.val + temp2.val == target:
                    result.append([temp1.val, temp2.val])
                temp2 = temp2.next
            temp1 = temp1.next
        
        return result
    # TC : O(n^2)
    # SC : O(1)
    
    def better_findPairsWithGivenSum(self, target):
        result = []    
        temp = self.head
        my_set = set()

        while temp:
            remainder = target - temp.val
            if remainder in my_set:
                result.append([remainder, temp.val])

            my_set.add(temp.val)
            temp = temp.next
        
        return result
    # TC : O(n)
    # SC : O(n)
    

    def findPairsWithGivenSum(self, target):
        left = self.head          # Left pointer starts at head (smallest element)
        right = self.head         # Right pointer will move to tail (largest element)
        ans = []            # List to store all valid pairs
        
        # Move right pointer to the end of the list
        while right.next:
            right = right.next
        
        # Use two pointers to find pairs
        while left is not None and right is not None and left.data < right.data:
            total = left.data + right.data  # Calculate sum of current pair
            
            if total == target:
                # Found a valid pair, add to results
                ans.append([left.data, right.data])
                left = left.next     # Move left pointer forward
                right = right.prev   # Move right pointer backward
            elif total > target:
                # Sum is too large, move right pointer to smaller element
                right = right.prev
            else:
                # Sum is too small, move left pointer to larger element
                left = left.next
        
        return ans
    # Tc = O(n) + O(n) == O(2n) == O(n)
    # Sc = O(1)



dll = DoublyLinkedList()
dll.insert_at_head(2)
dll.insert_at_head(1)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(8)
dll.append(9)
dll.traverse()
# dll.better_find_t(7)
# dll.brut_findPairsWithGivenSum(7)
dll.better_findPairsWithGivenSum(7)

