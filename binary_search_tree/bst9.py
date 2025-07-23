"""
230. Kth Smallest Element in a BST
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def better_kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        current = root

        while current :
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predessor = current.left

                while predessor.right and predessor.right != current:
                    predessor = predessor.right

                if predessor.right is None:
                    
                    predessor.right = current
                    current = current.left
                else:
                    predessor.right = None
                    result.append(current.val)
                    current = current.right
                
        return result[k-1]
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        count = 0

        while current :
            if current.left is None:
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                predessor = current.left

                while predessor.right and predessor.right != current:
                    predessor = predessor.right

                if predessor.right is None:
                    
                    predessor.right = current
                    current = current.left
                else:
                    predessor.right = None
                    count += 1
                    if count == k:
                        return current.val
                    current = current.right
    
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s = Solution()
print(s.kthSmallest(root, 3))

