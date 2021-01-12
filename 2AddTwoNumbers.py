class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        carry = 0
        while l1 or l2:
            # Check to see if we can end the loop early due to l1/l2 not existing
            if carry == 0:
                if not(l1):
                    node.next = l2
                    return head
                if not(l2):
                    node.next = l1
                    return head
            total = 0
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            total += carry
            # Break down amount to carry to next place 
            if total >= 10:
                carry = total // 10
                total = total % 10
            else:
                carry = 0
            # First iteration in loop, create head node
            if not(head):
                node = ListNode(total)
                head = node
            else:
                node.next = ListNode(total)
                node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            node.next = ListNode(carry)
        return head
