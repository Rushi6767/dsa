"""
Depth-First Search (DFS)
3. Postorder Traversal (Left → Right → Root)
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def postorder(root, result):
    if not root:
        return
    # Explore left
    postorder(root.left, result)
    # Explore right
    postorder(root.right, result)
    # Visit the root
    result.append(root.val)

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

# Run postorder traversal
res = []
postorder(root, res)
print(res)  # Output: [4, 5, 2, 6, 3, 1]

"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""