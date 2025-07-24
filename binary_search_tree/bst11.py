"""
98. Validate Binary Search Tree
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        current = root

        while current :
            if current.left is None:
                result.append(current.val)
                # print(current.val, end=" ")  # Directly process the value
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
                    # print(current.val, end=" ")  # Directly process the value
                    current = current.right

        for i in range(len(result) -1):
            if result[i] >= result[i+1]:
                return False
        return True
    
    # 2nd solution
    def solve(self, node, limit):
        if node is None:
            return None
        if not limit[0] < node < limit[1]:
            return False
        
        left = self.solve(node.left, [limit[0], node.val])
        if left == False:
            return False
        right = self.solve(node.right, [node.val, limit[1]])
        return left and right
    
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, [float("-inf"), float("inf")])
    
# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)

s = Solution()
print(s.isValidBST(root))