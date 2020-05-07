class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not(root):
            return False
        to_visit = [[root]]
        while to_visit:
            next_level_set = set()
            # Key = child node value, value = parent node value
            parent_dict = {}
            next_level = []
            curr_level = to_visit.pop()
            for node in curr_level:
                if node.left:
                    next_level_set.add(node.left.val)
                    next_level.append(node.left)
                    parent_dict[node.left.val] = node.val
                if node.right:
                    next_level_set.add(node.right.val)
                    next_level.append(node.right)
                    parent_dict[node.right.val] = node.val
            # Found both on next level.
            if (x in next_level_set) and (y in next_level_set):
                # Check for different parents
                if parent_dict[x] != parent_dict[y]:
                    return True
                else:
                    return False
            # Found one but not the other on next level.
            elif (x in next_level_set) or (y in next_level_set):
                return False
            if next_level:
                to_visit.append(next_level)
        return False
                
