class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def traverseAddRow(node, val, depth):
            if node is None:
                return 
            
            if depth == 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            
            traverseAddRow(node.left, val, depth - 1)
            traverseAddRow(node.right, val, depth - 1)
        
        if depth == 1:
            return TreeNode(val, root)

        traverseAddRow(root, val, depth-1)
        return root
