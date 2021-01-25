
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not(lists):
            return None
        # Merge linked lists two at a time until there is just one left
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    new_lists.append(self.merge_two(lists[i], lists[i+1]))
                else:
                    new_lists.append(lists[i])
            lists = new_lists.copy()
        return lists[0]
        
    def merge_two(self, A, B):
        if not(A):
            return B
        if not(B):
            return A
        head = None
        while A and B:
            if not(head):
                if A.val <= B.val:
                    head = A
                    A = A.next
                else:
                    head = B
                    B = B.next
                node = head
            else:
                if A.val <= B.val:
                    node.next = A
                    A = A.next
                else:
                    node.next = B
                    B = B.next
                node = node.next
        if A:
            node.next = A
        elif B:
            node.next = B
        return head
            
            
            
