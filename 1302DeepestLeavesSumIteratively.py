from collections import deque

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        to_traverse = deque()
        next_level = deque()
        next_level.append(root)
        to_traverse.append(next_level)
        # Step through each depth of the tree
        while to_traverse:
            current_level = to_traverse.popleft()
            next_level = deque()
            level_sum = 0
            # Step through the current depth and building the next depth to traverse. Keep track of the sum of each depth
            while current_level:
                current_node = current_level.popleft()
                level_sum += current_node.val
                if current_node.left:
                    next_level.append(current_node.left)
                if current_node.right:
                    next_level.append(current_node.right)
            if next_level:
                to_traverse.append(next_level)
        return(level_sum)
