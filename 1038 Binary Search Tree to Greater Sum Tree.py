class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        self.convert_tree(root)
        return root
        
    def convert_tree(self, root):
        if root.right:
            self.convert_tree(root.right)
        self.val += root.val
        root.val = self.val
        if root.left:
            self.convert_tree(root.left)