# 1028. Recover a Tree From Preorder Traversal
#
# We run a preorder depth-first search (DFS) on the root of a binary tree.
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
# If a node has only one child, that child is guaranteed to be the left child.
# Given the output traversal of this traversal, recover the tree and return its root.

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i, n = 0, len(traversal)
        deq = deque()
        root = None

        while i < n:
            depth = 0
            while traversal[i] == "-":
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i] != "-":
                value = value * 10 + int(traversal[i])
                i += 1

            if not root:
                root = TreeNode(value)
                deq.append((root, 0))
                continue

            while deq[-1][1] != depth - 1:
                deq.pop()

            if not deq[-1][0].left:
                node = TreeNode(value)
                deq[-1][0].left = node
                deq.append((node, depth))
            elif not deq[-1][0].right:
                node = TreeNode(value)
                deq[-1][0].right = node
                deq.append((node, depth))
            else:
                raise Exception("Unreachable")

        return root


# Solution().recoverFromPreorder("1-2--3--4-5--6--7")
# Solution().recoverFromPreorder("1-2--3---4-5--6---7")
# Solution().recoverFromPreorder("1-401--349---90--88")
