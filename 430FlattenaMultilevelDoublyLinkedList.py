class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.flatten_list(head)
        return head
    
    def flatten_list(self, head, parent=None):
        if not head:
            return
        save_head = head
        while head:
            if head.child:
                # Hold next node
                hold_next = head.next
                # Link to child
                head.next = head.child
                head.child.prev = head
                # Link to last node of the child list
                last_node = self.flatten_list(head.child, head)
                last_node.next = hold_next
                if hold_next:
                    hold_next.prev = last_node
                # Clear child
                head.child = None
            if head.next == None:
                last_node = head
            head = head.next
        return last_node
