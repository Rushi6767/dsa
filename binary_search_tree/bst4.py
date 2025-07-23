"""
Find the Floor in binary serch tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def Floor_bst(self, root, key):
        root = root
        floor = -1

        while root:
            if key == root.val:
                return root.val
            if key < root.val:
                root = root.left
            else:
                floor = root.val
                root = root.right
        return floor



root = TreeNode(11)
root.left = TreeNode(6)
root.right = TreeNode(16)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
# root.right.right = TreeNode(14)

s = Solution()
print(s.Floor_bst(root, 8))
print(s.Floor_bst(root, 14))

"""
Time complexity: O(log2 n)
Space complexity: O(1)
"""
