# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = deque()
        if not(root):
            return root
        to_visit = [[root]]
        while to_visit:
            next_level = deque()
            current_level = to_visit.pop()
            sub_ans = deque()
            for node in current_level:
                sub_ans.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ans.append(sub_ans)
            if next_level:
                to_visit.append(next_level)
        return ans
                
