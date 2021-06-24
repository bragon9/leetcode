# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        def reverse_ll(in_node):
            """Given a node, reverses (right-left) nodes and returns a head"""
            # Set dummy node that will connect to the rest of the linked list
            tail_dummy = ListNode(0)
            node = in_node
            prev = tail_dummy
            # Walk through reversing the list
            for i in range(right - left+1):
                hold = node.next
                node.next = prev
                prev = node
                node = hold
            # Link the tail of the reversed list to the next node after the reversed list
            in_node.next = hold
            # Return the head of the reversed list
            return prev
        
        # Walk through until we get to "left" node.
        node = dummy = ListNode(0, head)
        for i in range(left):
            prev = node
            node = node.next
        # Reverse the list
        prev.next = reverse_ll(node)
        # Return the head
        return dummy.next
