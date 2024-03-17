from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Consider all the leaves of a binary tree, from left to right order, the values 
# of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Solution: Traverse the left side of the tree first, adding any leaf nodes to a list, then move right.
# Then compare the leaf node lists of the two trees.
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    ans1, ans2 = [], []
    def leafTraverse(root, ans):
        if root:
            leafTraverse(root.left, ans)
            if root.left==None and root.right==None:
                ans.append(root.val)
            leafTraverse(root.right, ans)
    
    leafTraverse(root1, ans1)
    leafTraverse(root2, ans2)
    if ans1 == ans2:
        return True
    return False

binary_tree_1 = TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=2, left=TreeNode(val=7, left=None, right=None), right=TreeNode(val=4, left=None, right=None))), right=TreeNode(val=1, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=8, left=None, right=None)))
binary_tree_2 = TreeNode(val=3, left=TreeNode(val=5, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=7, left=None, right=None)), right=TreeNode(val=1, left=TreeNode(val=4, left=None, right=None), right=TreeNode(val=2, left=TreeNode(val=9, left=None, right=None), right=TreeNode(val=8, left=None, right=None))))
print(leafSimilar(binary_tree_1, binary_tree_2))