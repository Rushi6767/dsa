"""
Depth-First Search (DFS)
2. Inorder Traversal (Left → Root → Right)
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, result):
    if not root:
        return
    # Explore left
    inorder(root.left, result)
    # Visit the root
    result.append(root.val)
    # Explore right
    inorder(root.right, result)

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

# Run inorder traversal
res = []
inorder(root, res)
print(res)  # Output: [4, 2, 5, 1, 6, 3]

"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""