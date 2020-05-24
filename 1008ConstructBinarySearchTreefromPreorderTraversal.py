class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not(preorder):
            return None
        ptr = 0
        root = TreeNode(preorder[ptr])
        while ptr < len(preorder)-1:
            ptr += 1
            self.insert_node(root, preorder[ptr])
        return root
    
    def insert_node(self, root, val):
        node = TreeNode(val)
        while root.left or root.right:
            if root.left and val < root.val:
                root = root.left
            elif root.right and val > root.val:
                root = root.right
            else:
                break
        if val > root.val:
            root.right = node
        else:
            root.left = node
