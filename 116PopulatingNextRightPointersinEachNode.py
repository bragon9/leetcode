from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not(root):
            return root
        to_visit = deque()
        to_visit.append([root])
        # BFS
        while to_visit:
            next_level = []
            level = to_visit.popleft()
            # Loop through all nodes but last, setting "next" to the node to the right of them
            for i in range(len(level)-1):
                node = level[i]
                node.next = level[i+1]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # Set last node to None
            node = level[-1]
            node.next = None
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if next_level:
                to_visit.append(next_level)
        return root
