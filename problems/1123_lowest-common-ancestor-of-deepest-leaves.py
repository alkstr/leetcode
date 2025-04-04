# 1123. Lowest Common Ancestor of Deepest Leaves
#
# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
# Recall that:
# - The node of a binary tree is a leaf if and only if it has no children
# - The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# - The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return (0, None)

            left_depth, left_lca = _dfs(node.left)
            right_depth, right_lca = _dfs(node.right)

            if left_depth < right_depth:
                return (right_depth + 1, right_lca)
            elif left_depth > right_depth:
                return (left_depth + 1, left_lca)
            else:
                return (left_depth + 1, node)

        return _dfs(root)[1]
