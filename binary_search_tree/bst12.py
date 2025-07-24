"""
Lowest Common Ancestor [LCA] of a Binary Tree
"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # This function finds the path from root to the target node
    def find_path(self, root, target):
        path = []
        self.dfs(root, target, path)
        return path

    # Helper function to perform DFS and store the path
    def dfs(self, node, target, path):
        if node is None:
            return False

        # Add current node to the path
        path.append(node)

        # If this is the target node, we are done
        if node == target:
            return True

        # Recursively search in left or right subtree
        if self.dfs(node.left, target, path) or self.dfs(node.right, target, path):
            return True

        # If not found, remove the node from path (backtrack)
        path.pop()
        return False

    # Main function to find LCA
    def lowestCommonAncestor(self, root, p, q):
        # Find paths from root to p and q
        path_to_p = self.find_path(root, p)
        path_to_q = self.find_path(root, q)

        # Compare both paths and find the last common node
        i = 0
        while i < len(path_to_p) and i < len(path_to_q):
            if path_to_p[i] != path_to_q[i]:
                break
            i += 1

        # The last matched node is the LCA
        return path_to_p[i - 1]

# -----------------------------
# Build the binary tree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Use actual references to nodes for p and q
p = root.left              # Node with value 2
q = root.left.right        # Node with value 4

# Find LCA
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)

# Print result
print("Lowest Common Ancestor:", lca.val)  # Output: 2
