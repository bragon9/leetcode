class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not(t1):
            return t2
        self.merge(t1, t2)
        return t1
    
    def merge(self, t1, t2):
        # If no nodes, return None.
        if not(t1) and not(t2):
            return None
        # If there is only one node, return that node.
        if t1 and not(t2):
            return t1
        if not(t1) and t2:
            return t2
        # Set the children recursively.
        t1.left = self.merge(t1.left, t2.left)
        t1.right = self.merge(t1.right, t2.right)
        # There are two nodes. Set the new value and return the node.
        t1.val += t2.val
        return t1
        
