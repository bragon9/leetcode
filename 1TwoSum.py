class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        # Loop through and build a dictionary of all the indexes of the value.
        for index, value in enumerate(nums):
            if value in index_dict:
                index_dict[value] += [index]
                # If there are two and this number is half of target, we can return the answer now.
                if value * 2 == target:
                    return index_dict[value]
            else:
                index_dict[value] = [index]
        # Loop through all the keys and see if the corresponding number exists.
        for value in index_dict.keys():
            if value * 2 == target:
                continue
            if target - value in index_dict:
                return index_dict[value] + index_dict[target-value]
