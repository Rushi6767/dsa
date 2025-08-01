"""
700. Search in a Binary Search Tree
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root

        while temp:
            if temp.val == val:
                return temp
            elif val < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        return None
    

"""
Time complexity: O(log2 n)
Space complexity: O(1)
"""