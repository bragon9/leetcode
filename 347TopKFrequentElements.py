#from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        return heapq.nlargest(k, nums_dict, lambda x: nums_dict[x])
        
        ''' Old Answer
        count_dict = defaultdict(int)
        ans = []
        # Loop through and get occurrence count.
        for num in nums:
            count_dict[num] += 1
        k_ptr = 0
        # Loop desc through dictionary values adding keys to the answer array.
        for num, value in sorted(count_dict.items(), key=lambda x: -x[1]):
            k_ptr += 1
            ans.append(num)
            if k_ptr >= k:
                break
        return ans 
        '''
    
