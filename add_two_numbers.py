import unittest
from typing import Optional


class ListNode:
    """Singly-linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Add two numbers (medium).

        https://leetcode.com/problems/add-two-numbers/
        """
        # Initialize current node to dummy head of the returning list
        dummy_head = ListNode(0)
        result = dummy_head
        # Initialize carry to zero
        carry: int = 0
        # Loop through lists l1 and l2 until you reach both ends.
        while l1 is not None or l2 is not None:
            val1 = l1.val if l2 is not None and l1.val is not None else 0
            val2 = l2.val if l2 is not None and l2.val is not None else 0
            # set sum
            sum = carry + val1 + val2
            # update carry, either 0 or 1
            carry = int(sum / 10)
            # Create a new node with the digit value
            last_digit = sum % 10
            next_node = ListNode(last_digit)
            result.next = next_node
            # advance nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            result = result.next

        # check if carry is not zero, create new node
        if carry > 0:
            result.next = ListNode(carry)

        return dummy_head.next


class TestSolution(unittest.TestCase):
    def test_add_two_numbers(self):
        Solution.add_two_numbers(
            ListNode(2, ListNode(4, ListNode(3))),
            ListNode(5, ListNode(6, ListNode(4)))
        )


if __name__ == '__main__':
    unittest.main()
