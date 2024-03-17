from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Solution: Check if the rightmost child exists first and add the first element checked for each depth
def rightSideView(root: Optional[TreeNode]) -> list[int]:
    arr = []
    depth = 0

    def bfs(root, arr, depth):
        if root is None:
            return

        if depth == len(arr):
            arr.append(root.val)

        bfs(root.right, arr, depth+1)
        bfs(root.left, arr, depth+1)

    bfs(root, arr, depth)
    return arr

# Create a sample binary tree
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#     / 
#    10 

# Define the tree nodes
node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)
node10 = TreeNode(10)

# Connect the nodes to form the tree
node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4
node7.left = node10

print(rightSideView(node3))