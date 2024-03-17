from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree and an integer targetSum, return the number 
# of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must 
# go downwards (i.e., traveling only from parent nodes to child nodes).

# Solution: Keeps track of prefix sums while doing dfs to check if currentSum-prefixSum = targetSum
def pathSum(root: Optional[TreeNode], targetSum: int) -> int:     

        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            if root is None:
                return 0
            count = 0
            total += root.val
            # Can remove sums[currSum-targetSum] prefixSums to get target
            count = sums[total - targetSum]

            # Add value of this prefixSum
            sums[total] += 1
            count += dfs(root.left, total) + dfs(root.right, total)

            # Remove value of this prefixSum (path's been explored)
            sums[total] -= 1
            return count
        return dfs(root, 0)

# Slower than above
# Solution: For each node have it be the starting point for a new sum to try and get targetSum
# and seperately subtracted from all ongoing sums that pass it
def pathSum2(root: Optional[TreeNode], targetSum: int) -> int:     
        def dfs(root, target, include):
            if root is None:
                return 0
            count = 0
            if root.val == target:
                count += 1
            count += dfs(root.left, target - root.val, True) + dfs(root.right, target - root.val, True)
            if not include:
                count += dfs(root.left, target, False) + dfs(root.right, target, False)
            return count
        return dfs(root, targetSum, False)

binary_tree = TreeNode(val=10, left=TreeNode(val=5, left=TreeNode(val=3, left=TreeNode(val=3, left=None, right=None), right=TreeNode(val=-2, left=None, right=None)), right=TreeNode(val=2, left=None, right=TreeNode(val=1, left=None, right=None))), right=TreeNode(val=-3, left=None, right=TreeNode(val=11, left=None, right=None)))
print(pathSum(binary_tree, 8))
print(pathSum2(binary_tree, 8))