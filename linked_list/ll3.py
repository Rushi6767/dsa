"""
876. Middle of the Linked List
"""
# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution to find the middle node
class Solution:
    def middleNode(self, head):
        # Count the number of nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # # Go to the middle node
        # middle_index = count // 2
        # temp = head
        # for _ in range(middle_index):
        #     temp = temp.next

        return count

# Helper to build linked list from list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print a linked list from a given node
def print_linked_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

solution = Solution()
middle = solution.middleNode(head)

print("Second half of linked list:")
print_linked_list(middle)
