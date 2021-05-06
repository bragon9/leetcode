class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def split_arr(arr):
            if len(arr) == 1:
                return (None, arr[0], None)
            elif len(arr) == 2:
                return (None, arr[0], [arr[1]])
            else:
                mid_index = len(arr)//2
                return (arr[:mid_index], arr[mid_index], arr[mid_index+1:])
            
        def build_tree(arr):
            if not(arr):
                return
            l, m, r = split_arr(arr)
            node = TreeNode(m)
            if l:
                node.left = build_tree(l)
            if r:
                node.right = build_tree(r)
            return node
        
        vals_arr = []
        while head:
            vals_arr.append(head.val)
            head = head.next
        
        return build_tree(vals_arr)
