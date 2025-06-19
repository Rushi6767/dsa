"""
199. Binary Tree Right Side View
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def rightSideView(root):
    result = []
    right_view = []

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

    for i in result:
        right_view.append(i[-1])

    return right_view

"""
Time complexity : O(2n), Space complexity : O(n), if we include result then sc: O(n) + O(n)
"""

def rightSideView_better(root):
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

"""
Time complexity : O(n), Space complexity : O(n), if we include result then sc: O(n) + O(n)
"""

def reverse_postorder(root, level, result):
    if not root:
        return
    
    if level == len(result):
        result.append(root.val)

    if root.right:
        reverse_postorder(root.right,level+1, result)

    if root.left:
        reverse_postorder(root.left, level+1, result)

"""
Time complexity : O(n), Space complexity : O(H)
"""


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
levels = rightSideView(root)
# print(levels)  # Output: [[1], [2, 3], [4, 5, 6]]
# print(rightSideView_better(root))
res = []
reverse_postorder(root, 0, res)
print(res)


"""
Time complexity : O(n)
Space complexity : O(n)

if we include result then sc: O(n) + O(n)
"""