class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            nodes = []
            to_visit = [root]
            while to_visit:
                node = to_visit.pop()
                bisect.insort(nodes, node.val)
                if node.left:
                    to_visit.append(node.left)
                if node.right:
                    to_visit.append(node.right)
            return nodes
        
        def split(arr):
            if len(arr) == 1:
                return (arr[0], None, None)
            elif len(arr) == 2:
                return (arr[0], None, [arr[1]])
            mid = len(arr)//2 
            m = arr[mid]
            l = arr[:mid]
            r = arr[mid+1:]
            return (m, l, r)
        
        def build_tree(arr):
            if not(arr):
                return
            mid, l, r = split(arr)
            node = TreeNode(mid)
            if l:
                node.left = build_tree(l)
            if r:
                node.right = build_tree(r)
            return node
            
        vals_arr = traverse(root)
        return build_tree(vals_arr)
