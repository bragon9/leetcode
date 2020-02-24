class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not(root):
            return True
        to_visit = [[root]]
        # Loop through each level in the tree.
        while to_visit:
            # Array to store all the values of the nodes on this level.
            curr_level_vals = []
            # Array to store all the nodes on the next level.
            next_level = []
            nodes_to_visit = to_visit.pop()
            for node in nodes_to_visit:
                if node.left:
                    next_level.append(node.left)
                    curr_level_vals.append(node.left.val)
                else:
                    curr_level_vals.append(None)
                if node.right:
                    next_level.append(node.right)
                    curr_level_vals.append(node.right.val)
                else:
                    curr_level_vals.append(None)
            if next_level:
                to_visit.append(next_level)
            mid = len(curr_level_vals) // 2
            if curr_level_vals[:mid] != curr_level_vals[-1:mid-1:-1]:
                return False
        return True
                    
            
        
