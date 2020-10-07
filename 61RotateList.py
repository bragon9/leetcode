class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not(head):
            return None
        if not(head.next):
            return head
        node_vals = []
        while head:
            node_vals.append(head.val)
            if head.next:
                head = head.next
            else:
                break
        offset = k
        if k >= len(node_vals):
            offset = k % len(node_vals)
        node_vals = node_vals[-offset:]+node_vals[:-offset]
        root = ListNode(node_vals[0])
        node = root
        for val in node_vals[1:]:
            node.next = ListNode(val)
            node = node.next
        return root
