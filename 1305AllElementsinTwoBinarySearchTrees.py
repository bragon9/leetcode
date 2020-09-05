class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.r1 = []
        self.r2 = []
        ans = []
        # In order traversal each tree to get sorted values
        self.traverse(root1, self.r1)
        self.traverse(root2, self.r2)
        ptr1 = ptr2 = 0
        # Merge each list together
        while ptr1 < len(self.r1) and ptr2 < len(self.r2):
            num1 = self.r1[ptr1]
            num2 = self.r2[ptr2]
            if num1 <= num2:
                ans.append(num1)
                ptr1 += 1
            else:
                ans.append(num2)
                ptr2 += 1
        # If leftover, append to answer.
        if ptr1 < len(self.r1):
            ans += self.r1[ptr1:]
        elif ptr2 < len(self.r2):
            ans += self.r2[ptr2:]
        return ans
        
    def traverse(self, root, root_list):
        if not(root):
            return
        self.traverse(root.left, root_list)
        root_list.append(root.val)
        self.traverse(root.right, root_list)
            
