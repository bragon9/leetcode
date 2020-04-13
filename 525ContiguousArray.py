class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_dict = {0:0}
        running_total = 0
        ans = 0
        for i in range(len(nums)):
            print(i, nums[i])
            if nums[i] == 0:
                running_total -= 1
            else:
                running_total += 1
            if running_total in index_dict:
                sub_ans = i - index_dict[running_total]
                if running_total == 0:
                    sub_ans += 1
                ans = max(sub_ans, ans)
            else:
                index_dict[running_total] = i
        return ans
            
