"""
701. Insert into a Binary Search Tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def inseart_bst(self, root, val):
        if root is None:
            return TreeNode(val)
        temp = root
        while True:
            if val < temp.val :
                if temp.left == None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

val = 6

s = Solution()
print(s.inseart_bst(root, val))

"""
Time complexity: O(log2 n)
Space complexity: O(1)
"""