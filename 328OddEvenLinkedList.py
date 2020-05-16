class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # If not length 3, nothing to do.
        if not(head):
            return head
        if not head.next:
            return head
        if not head.next.next:
            return head
        self.switch_nodes(head, head.next)
        return head
    
    def switch_nodes(self, root, pre_forward):
        """Recursively loop through the linked list putting all the odd index nodes at the front"""
        if not(pre_forward.next):
            return
        forward = pre_forward.next
        forward_child = forward.next
        root_child = root.next
        root.next = forward
        forward.next = root_child
        pre_forward.next = forward_child
        if pre_forward.next:
            self.switch_nodes(forward, pre_forward.next)
        
