"""
Kth Largest Element in a BST
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def better_kthlargest(self, root: Optional[TreeNode], k: int) -> int:
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
                
        return result[-k]
    
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        # To get k-th largest, we reverse the order: Right → Root → Left (reverse inorder).
        current = root
        count = 0

        while current:
            if current.right is None:
                count += 1
                if count == k:
                    return current.val
                current = current.left
            else:
                predecessor = current.right
                while predecessor.left and predecessor.left != current:
                    predecessor = predecessor.left

                if predecessor.left is None:
                    predecessor.left = current
                    current = current.right
                else:
                    predecessor.left = None
                    count += 1
                    if count == k:
                        return current.val
                    current = current.left
    
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s = Solution()
print(s.kthLargest(root, 3))

