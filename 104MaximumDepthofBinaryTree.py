# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not(root):
#             return 0
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not(root):
            return 0
        ans = 0
        to_visit = [[root]]
        while to_visit:
            ans += 1
            level = to_visit.pop()
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                to_visit.append(new_level)
        return ans
