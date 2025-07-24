"""
Inorder successor in Binary Search Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def a_Find_successor(self, root, father):
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
                
        succesor = None
        for i in range(len(result)):
            if result[i] == father:
                if i != len(result) -1:
                    return result[i+1]
        return succesor
    
    def b_Find_successor(self, root, father):
        current = root
        suc = None

        while current :
            if current.left is None:
                if current.val == father:
                    suc = current.val
                elif suc != None:
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
                    if current.val == father:
                        suc = current.val
                    elif suc != None:
                        return current.val

                    current = current.right
        if suc == father:
            return None
        
    def c_Find_successor(self, root, father):
        current = root
        suc = None

        while current :
            if current.left is None:
                if current.val > father:
                    suc = current.val
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
                    if current.val > father:
                        suc = current.val
                    current = current.right
        return suc
    
    def d_Find_successor(self, root, key):
        current = root
        succesor = None

        while current:
            if current.val > key:
                succesor = current
                current = current.left
            else:
                current = current.right
        return succesor
    
    def Find_predesor(self, root, key):
        current = root
        predessor = None

        while current:
            if current.val < key:
                predessor = current
                current = current.left
            else:
                current = current.right
        return predessor

root = TreeNode(6)

root.left = TreeNode(3)
root.right = TreeNode(9)

root.left.left = TreeNode(2)
root.left.right = TreeNode(5)

root.left.left.left = TreeNode(1)
root.left.right.left = TreeNode(4)

root.right.left = TreeNode(8)
root.right.right = TreeNode(11)

root.right.left.left = TreeNode(7)
root.right.right.left = TreeNode(10)

s = Solution()

# print(s.b_Find_successor(root, 11))
print(s.d_Find_successor(root, 11))

"""
Time complexity : O(n)travers graph + O(n)result traverse = O(n)
space complexity : O(n) result

for b and c
Time complexity : O(n)
space complexity : O(1)

for d and predesor
Time complexity : O(log2 n) == O(H) == Height
space complexity : O(1)
"""