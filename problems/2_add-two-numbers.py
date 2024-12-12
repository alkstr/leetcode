# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(l: List[int]) -> Optional[ListNode]:
    first: Optional[ListNode] = None
    current: Optional[ListNode] = None

    for i in l:
        if not first:
            first = ListNode(i, None)
            current = first
        else:
            current.next = ListNode(i, None)
            current = current.next

    return first


def to_list(l: Optional[ListNode]) -> List[int]:
    result = []
    l_current = l

    while l_current:
        result.append(l_current.val)
        l_current = l_current.next

    return result


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_current = l1
        l2_current = l2
        l3_current: Optional[ListNode] = None

        l3_first: Optional[ListNode] = None
        overflow = False

        while l1_current or l2_current:
            result = 0
            if overflow:
                result += 1
                overflow = False

            result += (l1_current.val if l1_current else 0) + \
                (l2_current.val if l2_current else 0)

            if result > 9:
                overflow = True
                result -= 10

            if not l3_first:
                l3_first = ListNode(result, None)
                l3_current = l3_first
            else:
                l3_current.next = ListNode(result, None)
                l3_current = l3_current.next

            l1_current = l1_current.next if l1_current else None
            l2_current = l2_current.next if l2_current else None

        if overflow:
            l3_current.next = ListNode(1, None)

        return l3_first


assert to_list(
    Solution().addTwoNumbers(
        to_linked_list([2, 4, 3]),
        to_linked_list([5, 6, 4]))) == [7, 0, 8]

assert to_list(
    Solution().addTwoNumbers(
        to_linked_list([0]),
        to_linked_list([0]))) == [0]

assert to_list(
    Solution().addTwoNumbers(
        to_linked_list([9, 9, 9, 9, 9, 9, 9]),
        to_linked_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
