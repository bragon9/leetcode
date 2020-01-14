class Solution(object):    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.traverse(root)
        return self.ans
        
    def traverse(self, root):
        if not(root):
            return
        if root.left:
            self.traverse(root.left)
        self.ans.append(root.val)
        if root.right:
            self.traverse(root.right)
            
