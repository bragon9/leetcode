class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not(root):
            return 0
        self.ans = 0
        self.traverse(root.left, root.val, root.val)
        self.traverse(root.right, root.val, root.val)
        return self.ans
        
        
    def traverse(self, node, curr_min, curr_max):
        if not(node):
            return
        if node.val < curr_min:
            curr_min = node.val
        if node.val > curr_max:
            curr_max = node.val
        check_abs = abs(curr_min - curr_max)
        if check_abs > self.ans:
            self.ans = check_abs
        self.traverse(node.left, curr_min, curr_max)
        self.traverse(node.right, curr_min, curr_max)
