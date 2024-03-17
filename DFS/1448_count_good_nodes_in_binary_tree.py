# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given a binary tree root, a node X in the tree is named good 
# if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Solution: Recursively traverse tree and at each node which is the largest in its path to the root, add 1 and the number of good nodes in its children
def goodNodes(root: TreeNode) -> int:
    def dfs(root, path_max):
        if not root: 
            return 0
        if root.val >= path_max:
            return dfs(root.left, root.val) + dfs(root.right, root.val) + 1
        return dfs(root.left, path_max) + dfs(root.right, path_max)
    return dfs(root, root.val)

binary_tree = TreeNode(val=3, left=TreeNode(val=1, left=TreeNode(val=3, left=None, right=None), right=None), right=TreeNode(val=4, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=5, left=None, right=None)))
print(goodNodes(binary_tree))