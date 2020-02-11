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
        # Set min and max node
        if l1.val <= l2.val:
            min_node = l1
            max_node = l2
        else:
            min_node = l2
            max_node = l1
        if min_node.next:
            # If next min node is lesser than the current max node, keep it where it is
            if min_node.next.val < max_node.val:
                self.mergeTwoLists(min_node.next, max_node)
            # Max node should come next, so insert it 
            else:
                save_min_next = min_node.next
                save_max_next = max_node.next
                min_node.next = max_node
                min_node.next.next = save_min_next
                self.mergeTwoLists(min_node.next, save_max_next)
        # There is nothing else on this linked list, link the rest of the other list
        else:
            min_node.next = max_node
        return min_node
        
