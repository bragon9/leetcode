class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def traverseAddRow(node, val, depth):
            if node is None:
                return 
            
            if depth == 1:
                dummyLeft = TreeNode(val, node.left)
                dummyRight = TreeNode(val, None, node.right)
                node.left = dummyLeft
                node.right = dummyRight
                return
            
            traverseAddRow(node.left, val, depth - 1)
            traverseAddRow(node.right, val, depth - 1)
        
        if depth == 1:
            return TreeNode(val, root)

        traverseAddRow(root, val, depth-1)
        return root
