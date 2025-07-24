"""
235. Lowest Common Ancestor [LCA] of a Binary Search Tree
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        while True:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right

            elif p == current:
                return p
            elif q == current:
                return q
            
            else:
                return current

        

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
Time complexity : O(H)
space complexity : O(n) stack space
"""