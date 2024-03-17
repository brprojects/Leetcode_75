from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Solution: Store sum of each row in a dict during traversal
def maxLevelSum(root: Optional[TreeNode]) -> int:
        lvl_dict = defaultdict(int)
        lvl = 1

        def bfs(root, lvl_dict, lvl):
            if root is None:
                return

            lvl_dict[lvl] += root.val

            bfs(root.right, lvl_dict, lvl+1)
            bfs(root.left, lvl_dict, lvl+1)

        bfs(root, lvl_dict, lvl)
        return max(lvl_dict, key=lambda k: lvl_dict[k])

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

print(maxLevelSum(node3))