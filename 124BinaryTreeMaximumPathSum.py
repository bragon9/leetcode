class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root:
            self.max = root.val
        self.get_max(root)
        return self.max
    
    def get_max(self, root):
        if root == None:
            return None
        left = self.get_max(root.left)
        right = self.get_max(root.right)
        if left and right:
            self.max = max(self.max, root.val, root.val + left, 
                           root.val + right, root.val + left + right, 
                           left, right)
            return max(root.val, root.val + left, root.val + right)
        elif left:
            self.max = max(self.max, root.val, root.val + left, left)
            return max(root.val, root.val + left)
        elif right:
            self.max = max(self.max, root.val, root.val + right, right)
            return max(root.val, root.val + right)
        else:
            self.max = max(self.max, root.val)
            return root.val
