"""
450. Delete Node in a BST
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self,root, key):
        if root is None:
            return None
        
        if root.val == key:
            return self.deletion(root)
        
        temp = root
        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right
        return root
    
    def deletion(self, node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            right_child = node.right
            last_right = self.find_last_right(node.left)
            last_right.right = right_child
            return node.left
        
    def find_last_right(self, node):
        while node.right:
            node = node.right
        return node


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

val = 3
s = Solution()
print(s.deleteNode(root, val))

"""
Time complexity: O(log2 n)
Space complexity: O(1)
"""