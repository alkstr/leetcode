# 2415. Reverse Odd Levels of Binary Tree
#
# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_tree(l: List[int]) -> Optional[TreeNode]:
    n = len(l)
    root = TreeNode(l[0])
    deq = deque([root])
    i = 1

    while deq and i < n:
        current = deq.popleft()

        if i < n:
            current.left = TreeNode(l[i])
            deq.append(current.left)
            i += 1

        if i < n:
            current.right = TreeNode(l[i])
            deq.append(current.right)
            i += 1

    return root


def to_list(t: Optional[TreeNode]) -> List[int]:
    deq = deque([t])
    l = [t.val]

    while deq:
        current = deq.popleft()

        if current.left:
            l.append(current.left.val)
            deq.append(current.left)

        if current.right:
            l.append(current.right.val)
            deq.append(current.right)

    return l


def dfs(left: Optional[TreeNode], right: Optional[TreeNode], odd: bool):
    if not left or not right:
        return
    
    if odd:
        left.val, right.val = right.val, left.val

    odd = not odd
    dfs(left.left, right.right, odd)
    dfs(left.right, right.left, odd)


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs(root.left, root.right, True)
        return root


assert to_list(Solution().reverseOddLevels(
    to_tree([2, 3, 5, 8, 13, 21, 34]))) == [2, 5, 3, 8, 13, 21, 34]
assert to_list(Solution().reverseOddLevels(
    to_tree([7, 13, 11]))) == [7, 11, 13]
assert to_list(Solution().reverseOddLevels(
    to_tree([0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]))) == [0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]
