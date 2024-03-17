from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# Solution: Binary search where look left if val is larger than current node and right if smaller
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return
    if root.val == val:
        return root
    elif root.val > val:
        return searchBST(root.left, val)
    elif root.val < val:
        return searchBST(root.right, val)

# Create a sample binary tree
#         4
#        / \
#       2   7
#      / \ 
#     1   3


# Define the tree nodes
node4 = TreeNode(4)
node2 = TreeNode(2)
node7 = TreeNode(7)
node1 = TreeNode(1)
node3 = TreeNode(3)

# Connect the nodes to form the tree
node4.left = node2
node4.right = node7
node2.left = node1
node2.right = node3

print(searchBST(node4, 7).val)