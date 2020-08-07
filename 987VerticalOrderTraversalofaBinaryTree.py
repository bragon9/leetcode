from bisect import insort

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # key = Tuple coord, value = list of node values
        self.ans_dict = {}
        self.traverse(root, (0,0))
        # Sort dictionary by x asc, y desc
        self.ans_list = sorted(self.ans_dict.items(), key = lambda x: (x[0][0], -x[0][1]))
        prev = None
        ans = []
        sub_ans = []
        # Walk through and create answer list, sorted by node coordinate
        for coord, node_values in self.ans_list:
            (x, y) = coord
            if prev == None:
                prev = x
            if x != prev:
                prev = x
                ans.append(sub_ans)
                sub_ans = []
            for value in node_values:
                sub_ans.append(value)
        if sub_ans:
            ans.append(sub_ans)
        return ans
        
    def traverse(self, root, pos):
        """
        In-order traversal and add node info to dictionary
        """
        if not(root):
            return
        (x,y) = pos
        self.traverse(root.left, (x-1,y-1))
        if pos in self.ans_dict:
            insort(self.ans_dict[pos], root.val)
        else:
            self.ans_dict[pos] = [root.val]
        self.traverse(root.right, (x+1,y-1))
        
        
