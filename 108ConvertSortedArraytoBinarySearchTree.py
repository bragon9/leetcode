class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not(nums):
            return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        if mid < len(nums)-1:
            node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
