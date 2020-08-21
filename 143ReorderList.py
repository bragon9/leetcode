class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not(head) or not(head.next) or not(head.next.next):
            return
        fast = head
        slow = head
        ptr = 0
        while fast.next:
            fast = fast.next
            if ptr % 2 != 0:
                slow = slow.next
            ptr += 1
        halfway = slow.next
        slow.next = None        
        # reverse 2nd half
        prev = None
        while halfway:
            nxt = halfway.next
            halfway.next = prev
            prev = halfway
            halfway = nxt
        end = prev
        
        while end:
            head_next = head.next
            end_next = end.next
            head.next = end
            end.next = head_next
            head = head_next
            end = end_next

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not(head) or not(head.next):
#             return
#         node = head
#         arr = []
#         while node:
#             arr.append(node)
#             node = node.next
#         f = 0
#         b = len(arr)-1
#         ans_arr = []
#         while f <= b:
#             if f == b:
#                 ans_arr.append(arr[f])
#                 break
#             ans_arr.append(arr[f])
#             ans_arr.append(arr[b])
#             f += 1
#             b -= 1
#         node = ans_arr[0]
#         for i in range(1, len(ans_arr)):
#             node.next = ans_arr[i]
#             node = node.next
#         node.next = None
