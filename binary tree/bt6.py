"""
543. Diameter of Binary Tree
"""
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    max_diameter = [0]  # list to make it mutable inside helper

    def height(node):
        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)

        # Update the diameter at each node
        max_diameter[0] = max(max_diameter[0], left + right)

        # Return height of the current subtree
        return 1 + max(left, right)

    height(root)
    return max_diameter[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)

print(diameter_of_binary_tree(root))

"""
Time complexity : O(n)
Space complexity : O(H)

where H is Height of Binary tree (numbers of level)
"""