class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        sub_total = 0
        # Loop through keeping a running total
        for index, value in enumerate(nums):
            if value > 0:
                # If the value alone is higher than the running total, reset running total to value
                if value > value + sub_total:
                    sub_total = value
                else:
                    sub_total += value
            # Always keep running total of negative numbers.  
            else:
                sub_total += value
                # Covers case where all values are negative.  
                max_total = max(value, max_total)
            max_total = max(max_total, sub_total)
        return max_total
        
#         ## FAILED TIME - Check from positive numbers brute force
#         ans = nums[0]
#         self.nums = nums
#         self.max_index = len(nums)
#         for index, value in enumerate(nums):
#             if value > 0:
#                 ans = max(ans, self.check_left_sum(index), self.check_right_sum(index))
#             else:
#                 ans = max(ans, value)
#         return ans
    
#     def check_left_sum(self, index):
#         total = 0
#         max_total = self.nums[index]
#         for ptr in range(index, -1, -1):
#             total += self.nums[ptr]
#             max_total = max(total, max_total)
#         return max_total

#     def check_right_sum(self, index):
#         total = 0
#         max_total = self.nums[index]
#         for ptr in range(index, self.max_index):
#             total += self.nums[ptr]
#             max_total = max(total, max_total)
#         return max_total                
        
        ## FAILED SPACE - Save off sums into dict, brute force
        # ans = nums[0]
        # sum_dict = {}
        # for window_size in range(1, len(nums)+1):
        #     for start in range(len(nums)):
        #         end = start+window_size
        #         if end > len(nums):
        #             break
        #         if window_size > 1:
        #             window_sum = sum_dict[(start, end-1)] + nums[end-1]
        #         else:
        #             window_sum = sum(nums[start:end])
        #         sum_dict[(start, end)] = window_sum
        #         ans = max(window_sum, ans)
        # return ans
               
        ## FAILED TIME - Sliding windows brute force
        # ans = nums[0]
        # for window_size in range(1, len(nums)+1):
        #     for index in range(len(nums)):
        #         if index+window_size > len(nums):
        #             break
        #         ans = max(sum(nums[index:index+window_size]), ans)
        # return ans
       
