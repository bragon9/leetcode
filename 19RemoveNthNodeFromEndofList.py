class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        f = b = head
        # Set up two pointers and advance the first pointer n times. Then remove b.next to remove "nth" node from the end.
        for _ in range(n):
            f = f.next
        if f:
            while f.next:
                b = b.next
                f = f.next
            b.next = b.next.next
        else:
            if b.next:
                dummy.next = b.next
            else:
                dummy.next = None
        return dummy.next
