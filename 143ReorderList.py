class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not(head) or not(head.next):
            return
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next
        f = 0
        b = len(arr)-1
        ans_arr = []
        while f <= b:
            if f == b:
                ans_arr.append(arr[f])
                break
            ans_arr.append(arr[f])
            ans_arr.append(arr[b])
            f += 1
            b -= 1
        node = ans_arr[0]
        for i in range(1, len(ans_arr)):
            node.next = ans_arr[i]
            node = node.next
        node.next = None
