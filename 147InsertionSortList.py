class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next
        if sorted_list:
            sorted_list = sorted(sorted_list)
            start = ListNode(sorted_list[0])
            node = start
            for i in range(1, len(sorted_list)):
                new_node = ListNode(sorted_list[i])
                node.next = new_node
                node = node.next
            node.next = None
        else:
            return None
        return start


# class Solution:
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         sorted_head = None
#         to_sort = head
#         while to_sort:
#             hold = to_sort.next
#             sorted_head = self.node_sort(to_sort, sorted_head)
#             to_sort = hold
#         return sorted_head
            
#     def node_sort(self, node, head):
#         prev = None
#         if head:
#             start = head
#         else:
#             node.next = None
#             return node
#         # Loop through already sorted nodes
#         while head:
#             # Node should be inserted
#             if node.val < head.val:
#                 if prev:
#                     hold = prev.next
#                     prev.next = node
#                     node.next = head
#                     return start
#                 else:
#                     node.next = head
#                     return node
#             prev = head
#             head = head.next
#         prev.next = node
#         node.next = None
#         return start
