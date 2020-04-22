class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_dict = {}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total in sum_dict:
                sum_dict[total].append(i)
            else:
                sum_dict[total] = [i]
        for value, index_list in sum_dict.items():
            if value == k:
                ans += len(index_list)
            search_value = value - k
            if search_value in sum_dict:
                for index in index_list:
                    for search_index in sum_dict[search_value]:
                        if search_index < index:
                            ans += 1
        return ans
            
            
           
