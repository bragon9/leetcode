lass Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not(root):
            return root
        self.values = []
        self.traverse(root)
        return self.create_tree(root, self.values)
        
    def traverse(self, node):
        if not(node):
            return
        self.traverse(node.left)
        self.values.append(node.val)
        self.traverse(node.right)
        
    def create_tree(self, root, values):
        root = TreeNode(values[0])
        node = root
        for val in values[1:]:
            node.right = TreeNode(val)
            node = node.right
        return root
