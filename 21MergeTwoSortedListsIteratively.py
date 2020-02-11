# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not(l1) and not(l2):
            return None
        if not(l1):
            return l2
        if not(l2):
            return l1
        # Use the linked list with the lowest head to merge into.
        if l1.val <= l2.val:
            head = l1
            other = l2
        else:
            head = l2
            other = l1
        answer = head
        while head.next and other:
            # If the next head value is lower than other, keep looping through head.
            if head.next.val <= other.val:
                head = head.next
            else:
                # Insert other into the next head node.
                next_other = other.next
                next_head = head.next
                head.next = other
                head.next.next = next_head
                other = next_other
                head = head.next
        # If there is any left over, append to head.
        if other:
            head.next = other            
        return answer
            
            
            
