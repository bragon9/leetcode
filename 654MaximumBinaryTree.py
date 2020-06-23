class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not(nums):
            return None
        max_val = 0
        max_index = 0
        for index, value in enumerate(nums):
            if value > max_val:
                max_val = value
                max_index = index
        left_arr = nums[:max_index]
        right_arr = nums[max_index+1:]
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(left_arr)
        root.right = self.constructMaximumBinaryTree(right_arr)
        return root
