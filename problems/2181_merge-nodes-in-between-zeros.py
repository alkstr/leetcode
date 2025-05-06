# 2181. Merge Nodes in Between Zeros
#
# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        new_head = ListNode()
        new_current = new_head
        while current:
            while current.val != 0:
                new_current.val += current.val
                current = current.next

            if current.next:
                new_current.next = ListNode()
                new_current = new_current.next

            current = current.next

        return new_head
