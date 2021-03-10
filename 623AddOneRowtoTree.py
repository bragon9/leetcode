class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not(root):
            return
        if d == 1:
            return TreeNode(v, root)
        to_visit = [[root]]
        depth = 1
        while to_visit:
            lvl = to_visit.pop()
            depth += 1
            next_lvl = []
            if depth == d:
                self.add_depth(lvl, v)
                return root
            else:
                for node in lvl:
                    if node.left:
                        next_lvl.append(node.left)
                    if node.right:
                        next_lvl.append(node.right)
            if next_lvl:
                to_visit.append(next_lvl)
        
    def add_depth(self, level, value):
        for node in level:
            if node.left:
                hold = node.left
                node.left = TreeNode(value, hold)
            else:
                node.left = TreeNode(value)
            if node.right:
                hold = node.right
                node.right = TreeNode(value, None, hold)
            else:
                node.right = TreeNode(value)
