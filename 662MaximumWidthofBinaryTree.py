class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.traverse([root])
        return self.ans
    
    def traverse(self, level):
        if not(level):
            return
        next_level = []
        width = len(level)
        self.ans = max(width, self.ans)
        # BFS by level
        for node in level:
            if node == None:
                next_level.extend([None, None])
                continue
            if node.left:
                next_level.append(node.left)
            else:
                next_level.append(None)
            if node.right:
                next_level.append(node.right)
            else:
                next_level.append(None)
        start = None
        end = None
        ptr = 0
        while ptr < len(next_level):
            if next_level[ptr]:
                start = ptr
                break
            ptr += 1
        ptr = len(next_level)-1
        if start != None:
            while ptr >= start:
                if next_level[ptr]:
                    end = ptr
                    break
                ptr -= 1
            self.traverse(next_level[start:end+1])
