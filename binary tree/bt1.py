"""
Depth-First Search (DFS)
1. Preorder Traversal (Root → Left → Right)
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def preorder(root, result):
    if not root:
        return
    # Visit the root
    result.append(root.val)
    # Explore left
    preorder(root.left, result)
    # Explore right
    preorder(root.right, result)

# Build the binary tree:
#         1
#       /   \
#      2     3
#     / \   /
#    4   5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)

# Run preorder traversal
res = []
preorder(root, res)
print(res)  # Output: [1, 2, 4, 5, 3, 6]

"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""