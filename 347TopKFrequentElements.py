from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
    
