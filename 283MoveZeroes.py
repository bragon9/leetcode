class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                num_zeros += 1
                nums.pop(i)
            else:
                i += 1
        return nums.extend([0] * num_zeros)
