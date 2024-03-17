from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

# Solution: At each step if their is a node present, either continue the current zigzag or start a new zigzag
def longestZigZag(root: Optional[TreeNode]) -> int:
    maxLength = 0
    def dfs(node, depth, dir):
        nonlocal maxLength
        maxLength = max(maxLength, depth)

        if node.left is not None:
            dfs(node.left, depth+1, 'left') if dir != 'left' else dfs(node.left, 1, 'left')
        if node.right is not None:
            dfs(node.right, depth+1, 'right') if dir != 'right' else dfs(node.right, 1, 'right')
    dfs(root, 0, '')
    return maxLength

binary_tree = TreeNode(val=1, left=None, right=TreeNode(val=1, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=1, left=TreeNode(val=1, left=None, right=TreeNode(val=1, left=None, right=TreeNode(val=1, left=None, right=None))), right=TreeNode(val=1, left=None, right=None))))
print(longestZigZag(binary_tree))