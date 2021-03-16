class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not(s):
            return None
        node, rest = self.getNode(s)
        l, r = self.getChildren(rest)
        return TreeNode(node, self.str2tree(l), self.str2tree(r))
        
    def getNode(self, s):
        for index, value in enumerate(s):
            if value == '(':
                return int(s[:index]), s[index:]
        return int(s), None
    
    def getChildren(self, s):
        if not(s):
            return None, None
        ctr = 0
        for index, value in enumerate(s):
            if value == '(':
                ctr += 1
            elif value == ')':
                ctr -= 1
            if ctr == 0:
                if index + 2 > len(s):
                    return s[1:index], None
                else:
                    return s[1:index], s[index+2:-1]
