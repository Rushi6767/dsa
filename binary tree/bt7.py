"""
110. Balanced Binary Tree
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    
    left_h = height(root.left)
    if left_h == -1:
        return -1
    
    right_h = height(root.right)
    if right_h == -1:
        return -1
    
    if abs(left_h - right_h) > 1:
        return -1
    
    l= 1 + max(left_h, right_h)
    return l

def isBalanced(root):
    x = height(root)
    if x == -1:
        return False
    return True 

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)

print(isBalanced(root))


"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""