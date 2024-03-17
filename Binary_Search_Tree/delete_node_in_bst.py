from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given a root node reference of a BST and a key, delete the node with the given 
# key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:
# 1. Search for a node to remove.
# 2. If the node is found, delete the node.

# Solution: Find the node to remove, then if it has one child just attach the other child.
# But if it has two children find the smallest value node in the right tree and replace the node to be removed's value with it,
# then remove the smallest value node
def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    
    def findmin(root):
        while root != None and root.left != None:
            root = root.left
        return root

    def remove(root, key):
        if root == None:
            return
        if key > root.val:
            root.right = remove(root.right, key)
        elif key < root.val:
            root.left = remove(root.left, key)
        elif key == root.val:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                minNode = findmin(root.right)
                root.val = minNode.val
                root.right = remove(root.right, minNode.val)
        return root

    return remove(root, key)

# Create a sample binary tree
#         5
#        / \
#       3   6
#      / \   \ 
#     2   4   7


# Define the tree nodes
node5 = TreeNode(5)
node3 = TreeNode(3)
node6 = TreeNode(6)
node2 = TreeNode(2)
node4 = TreeNode(4)
node7 = TreeNode(7)

# Connect the nodes to form the tree
node5.left = node3
node5.right = node6
node3.left = node2
node3.right = node4
node6.right = node7

print(deleteNode(node4, 3))