
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert_tree(root, 0)
        return root
              
    def convert_tree(self, root, ans):
        if not(root):
            return ans
        if root.right:
            self.convert_tree(root.right, ans)
        ans += root.val
        print(root.val, ans)
        if root.left:
            self.convert_tree(root.left, ans)
