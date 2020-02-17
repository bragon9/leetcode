class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.get_diameter(root)
        return self.ans
        
    def get_diameter(self, node):
        if not(node):
            return 0
        # Get longest length through left child.
        left_depth = self.get_diameter(node.left)
        # Get longest length through right child.
        right_depth = self.get_diameter(node.right)
        # The longest leg of the left or the right.
        longest_leg = max(left_depth, right_depth)
        # The longest path through this node.
        longest_path = left_depth + right_depth
        if longest_path > self.ans:
            self.ans = longest_path
        return longest_leg + 1
        
