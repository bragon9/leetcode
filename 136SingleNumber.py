from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = defaultdict(int)
        for i in range(len(nums)):
            num_dict[nums[i]] += 1
        for key, value in num_dict.items():
            if value == 1:
                return key
