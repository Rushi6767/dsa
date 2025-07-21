"""
find minimum in Binary Search Tree
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def Minimum_searchBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root

        while temp:
            if temp.left == None:
                return temp.val
            temp = temp.left
    
root = TreeNode(9)
root.left = TreeNode(2)
root.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(15)

s = Solution()
print(s.Minimum_searchBST(root))

"""
Time complexity: O(log2 n)
Space complexity: O(1)
"""