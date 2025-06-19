"""
124. Binary Tree Maximum Path Sum
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    maxi = float("-inf")

    def helper(node):
        nonlocal maxi
        if not node:
            return 0

        left_sum = helper(node.left)
        if left_sum < 0:
            left_sum = 0

        right_sum = helper(node.right)
        if right_sum < 0:
            right_sum = 0

        maxi = max(maxi, left_sum + node.val + right_sum)

        return node.val + max(left_sum, right_sum)

    helper(root)
    return maxi


root = TreeNode(-10)
root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxPathSum(root))  # Output should be 42

"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""