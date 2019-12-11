# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.sum = 0
        self.L = L
        self.R = R
        self.return_sum(root)
        return self.sum
        
    def return_sum(self, node):
        if not(node):
            return
        # If node is within bounds, add to sum.
        if node.val >= self.L and node.val <= self.R:
            self.sum += node.val
        # If child has possibility to be within bounds, call function.
        if node.left and node.val >= self.L:
            self.return_sum(node.left)
        if node.right and node.val <= self.R:
            self.return_sum(node.right)
