class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def traverse_to_depth(node, depth):
            curr_lvl = [node]
            next_lvl = []
            for _ in range(depth - 2):
                for curr_node in curr_lvl:
                    if curr_node.left:
                        next_lvl.append(curr_node.left)
                    if curr_node.right:
                        next_lvl.append(curr_node.right)
                        
                curr_lvl, next_lvl = next_lvl, []
            
            return curr_lvl
        
        def add_child(node, filler_node):
            hold_left = node.left
            hold_right = node.right
            
            node.left = deepcopy(filler_node)
            node.right = deepcopy(filler_node)
            
            node.left.left = hold_left
            node.right.right = hold_right
        
        filler_node = TreeNode(val)
        
        if depth == 1:
            filler_node.left = root
            return filler_node
        
        parent_nodes = traverse_to_depth(root, depth)
        
        for parent in parent_nodes:
            add_child(parent, filler_node)
        
        return root
