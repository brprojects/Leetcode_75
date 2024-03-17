from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along 
# the longest path from the root node down to the farthest leaf node.

# Solution: Depth first search where return the largest depth of the left and right branches recursively, then if a leaf node is reached return depth
def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        if not root:
            return depth
        else:
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    return dfs(root, 0)

binary_tree = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None), right=TreeNode(val=7, left=None, right=None)))
print(maxDepth(binary_tree))