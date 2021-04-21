# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traverse(node):
            if not(node):
                return
            self.ans.append(node.val)
            for child in node.children:
                traverse(child)
            
        self.ans = []
        traverse(root)
        return self.ans
      
# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not(root):
            return None
        stack = collections.deque()
        to_visit = [root]
        ans = []
        while to_visit:
            node = to_visit.pop()
            ans.append(node.val)
            for child in node.children[::-1]:
                to_visit.append(child)
        return ans
