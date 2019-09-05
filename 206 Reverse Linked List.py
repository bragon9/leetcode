class Solution(object):
    def reverseList(self, head, prev=None):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    while head:
        next_node = head.next
        head.next = prev
        return self.reverseList(next_node, head)
    return prev