# 889. Construct Binary Tree from Preorder and Postorder Traversal
#
# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
# If there exist multiple answers, you can return any of them.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre, post = 0, 0

        def _make_tree() -> Optional[TreeNode]:
            nonlocal pre, post
            root = TreeNode(preorder[pre])
            pre += 1

            if root.val != postorder[post]:
                root.left = _make_tree()

            if root.val != postorder[post]:
                root.right = _make_tree()

            post += 1
            return root

        return _make_tree()


# Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
# Solution().constructFromPrePost([1], [1])
