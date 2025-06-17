"""
Breadth-First Search (BFS)
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Perform a BFS (level-order) traversal on a binary tree and
    return a list of levels, where each level is a list of node values.
    """
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

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

# Run level-order traversal
levels = level_order_traversal(root)
print(levels)  # Output: [[1], [2, 3], [4, 5, 6]]

"""
Time complexity : O(n)
Space complexity : O(n)

if we include result then sc: O(n) + O(n)
"""