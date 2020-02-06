class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.ans_len = len(nums)
        used_nums = set()
        chain = [None] * self.ans_len
        self.breakdown(chain, 0, used_nums)
        return self.ans
        
    def breakdown(self, chain, index, used_nums):
        # If we have a full answer, add to list and return.
        if index == self.ans_len:
            self.ans.append(chain)
            return
        # Make a local copy of chain to manipulate.
        local_chain = chain.copy()
        # Loop through all the numbers in nums and insert into chain at index point, then move to next index.
        for num in self.nums:
            if num in used_nums:
                continue
            local_chain[index] = num
            local_used_nums = used_nums.copy()
            local_used_nums.add(num)
            self.breakdown(local_chain, index+1, local_used_nums)
