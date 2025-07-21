"""
Find the ceil in binary serch tree
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   
    def findCeil(self,root, inp):
        temp = root
        ceil = -1

        while temp:
            if temp.val == inp:
                return temp.val
            elif inp < temp.val:
                ceil = temp.val
                temp = temp.left
            else:
                ceil = temp.val
                temp = temp.right
        return ceil

    
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)

s = Solution()
print(s.findCeil(root, 5))   # Expected output: 6
print(s.findCeil(root, 1))   # Expected output: 2
print(s.findCeil(root, 15))  # Expected output: 14 (or last max, depending how you treat > max)
print(s.findCeil(root, 8))

"""
Time complexity: O(log2 n)
Space complexity: O(1)
"""