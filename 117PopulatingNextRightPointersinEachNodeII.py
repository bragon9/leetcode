class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not(root):
            return 
        to_visit = [[root]]
        while to_visit:
            level = to_visit.pop()
            next_level = []
            for i in range(len(level)-1):
                node = level[i]
                node.next = level[i+1]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            node = level[-1]
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if next_level:
                to_visit.append(next_level)
        return root
