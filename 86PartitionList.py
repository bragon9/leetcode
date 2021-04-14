class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create a left list to hold values < x, and a right list for values >= x
        l = ListNode(None)
        r = ListNode(None)
        l_head = l
        r_head = r
        # Walk through the given list and create our two lists.
        while head:
            if head.val < x:
                l.next = ListNode(head.val)
                l = l.next
            else:
                r.next = ListNode(head.val)
                r = r.next
            head = head.next
        # Join right list to end of left list
        l.next = r_head.next
        r_head.next = None
        return l_head.next
