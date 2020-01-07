from collections import deque

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth_arr = deque()
        depth_arr.append(root)
        return self.findDepthSum(depth_arr, 0, 0)
    
    def findDepthSum(self, depth_arr, prev_total, new_total):
        """
        Step through each depth keeping track of the sum
        """
        # If there are nodes on this depth, return the sum of the previous depth
        if not(depth_arr):
            return prev_total
        new_depth_arr = deque()
        depth_total = 0
        # Step through each node in this depth adding the children to the next depth.  Keep track of the sum.
        while depth_arr:
            node = depth_arr.popleft()
            depth_total += node.val
            if node.left:
                new_depth_arr.append(node.left)
            if node.right:
                new_depth_arr.append(node.right)
        return self.findDepthSum(new_depth_arr, depth_total, 0)
