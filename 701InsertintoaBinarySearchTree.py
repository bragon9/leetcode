class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.val = val
        self.insert_node(root)
        return root
        
    def insert_node(self, node):
        if not(node):
            return
        if self.val > node.val:
            if node.right:
                self.insert_node(node.right)
            else:
                node.right = TreeNode(self.val)
        if self.val < node.val:
            if node.left:
                self.insert_node(node.left)
            else:
                node.left = TreeNode(self.val)
