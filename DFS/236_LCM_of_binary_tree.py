# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T that 
# has both p and q as descendants (where we allow a node to be a descendant of itself).

# Solution: Finds the LCM by finding one of p or q then making sure the other side of the branch doesn't contain the other of p or q
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        l = lowestCommonAncestor(root.left, p, q)
        r = lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r

# Create a sample binary tree
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4

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

# Connect the nodes to form the tree
node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

print(lowestCommonAncestor(node3, node0, node8).val)