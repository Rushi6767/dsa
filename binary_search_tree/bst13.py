"""
Lowest Common Ancestor [LCA] of a Binary Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, node, p, q):
        if node is None:
            return None
        if node ==p or node== q:
            return node
        left = self.solve(node.left, p, q)
        right = self.solve(node.right, p, q)

        if left is None and right is None:
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        return node


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root, p, q)
        

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

s = Solution()

# Reference actual nodes
p = root.left       # TreeNode(2)
q = root.right
lca = s.lowestCommonAncestor(root,p, q)
print(lca.val)

"""
Time complexity : O(n)
space complexity : O(n) stack space
"""