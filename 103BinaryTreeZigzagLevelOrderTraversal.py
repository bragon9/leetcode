class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not(root):
            return
        self.ans = []
        self.traverse([root], False)
        return self.ans
        
    def traverse(self, level, reverse):
        if not(level):
            return
        next_level = []
        sub_ans = []
        for node in level:
            sub_ans.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if reverse:
            self.ans.append(sub_ans[::-1])
        else:
            self.ans.append(sub_ans)
        self.traverse(next_level, not(reverse))
