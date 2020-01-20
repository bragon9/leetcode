from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        to_visit = deque()
        to_visit.append(root)
        processed_dict = {}
        ans = deque()
        if not(root):
            return None
        while to_visit:
            current_node = to_visit.pop()
            if current_node.left and (hash(current_node.left) not in processed_dict):
                to_visit.append(current_node)
                to_visit.append(current_node.left)
                continue
            if hash(current_node) not in processed_dict:
                ans.append(current_node.val)
                processed_dict[hash(current_node)] = 1
            if current_node.right:
                to_visit.append(current_node.right)
        return ans
