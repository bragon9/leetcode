# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        digits = []
        # Make a list of string digit values
        while head:
            digits.append(str(head.val))
            head = head.next
        # Join into one long string and display as base 2 int
        return int(''.join(digits), 2)
