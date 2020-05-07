class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
# No duplicate values allowed version:
#         to_visit = [cloned]
#         while to_visit:
#             curr_node = to_visit.pop()
#             if curr_node.val == target.val:
#                 return curr_node
#             if curr_node.left:
#                 to_visit.append(curr_node.left)
#             if curr_node.right:
#                 to_visit.append(curr_node.right)

# Duplicate values allowed version:
        self.target = target
        path = self.find_target_path(original, [])
        return self.find_clone(cloned, path)
    
    def find_target_path(self, node, path):
        """Find the path to the target node"""
        if not(node):
            return 
        if node == self.target:
            return path
        return self.find_target_path(node.left, path + ['L']) or self.find_target_path(node.right, path + ['R'])
        
    def find_clone(self, cloned, path):
        """Follow the path to the cloned node"""
        node = cloned
        ptr = 0
        while ptr < len(path):
            if path[ptr] == 'R':
                node = node.right
            else:
                node = node.left
            ptr += 1
        return node
            
