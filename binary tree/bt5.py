"""
104. Maximum Depth of Binary Tree
"""

# from collections import deque

# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None

# def maxDepth(root) -> int:
#         count = 0
#         if not root:
#             return 0

#         queue = deque([root])

#         while queue:
#             level_size = len(queue)
#             current_level = []
#             count += 1

#             for _ in range(level_size):
#                 node = queue.popleft()
#                 current_level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return count

# # Build the binary tree:
# #         1
# #       /   \
# #      2     3
# #     / \   /
# #    4   5 6

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# root.right = TreeNode(3)
# root.right.left = TreeNode(6)

# # Run level-order traversal
# levels = maxDepth(root)
# print(levels)
# """
# Time complexity : O(n)
# Space complexity : O(n)
# """

# # ========recursive (DFS)============
"""
Use recursive ==> optimal solution
"""
def solve(node):
    if node == None:
        return 0
    
    left_h = solve(node.left)
    right_h = solve(node.right)
    return 1 + max(left_h, right_h)

"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""