# 1261. Find Elements in a Contaminated Binary Tree
#
# Given a binary tree with the following rules:
# - root.val == 0
# - For any treeNode:
#   - If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
#   - If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
# Implement the FindElements class:
# - FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# - bool find(int target) Returns true if the target value exists in the recovered binary tree.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        root.val = 0
        deq = deque([root])

        while deq:
            current = deq.popleft()
            self.values.add(current.val)
            if current.left:
                deq.append(current.left)
                current.left.val = 2 * current.val + 1
            if current.right:
                deq.append(current.right)
                current.right.val = 2 * current.val + 2

    def find(self, target: int) -> bool:
        return target in self.values
