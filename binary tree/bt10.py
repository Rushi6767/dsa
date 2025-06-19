"""
Bottom View of Binary Tree
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return None
    
    ans =[]
    queue = deque()
    result = {}
    
    queue.append((root, 0))

    while queue:
        e, line = queue.popleft()
        # if line not in result:
        result[line] = e.val
        if e.left:
            queue.append((e.left, line-1))
        if e.right:
            queue.append((e.right, line + 1))

    for value in sorted(result.items()):
        ans.append(value[1])

    return ans

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
print(bottom_view(root))

"""
Time complexity : O(n) + O(nlogn) + O(n)
Space complexity : O(n) + O(n)
"""