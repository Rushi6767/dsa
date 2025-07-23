"""
Morris algorithm for inorder traversal
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self,root):
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
                
        return result
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s = Solution()
print(s.inorderTraversal(root))

"""
Time complexity : O(n)
space complexity : O(n) if take result list

space complexity : O(1) if use print()
"""