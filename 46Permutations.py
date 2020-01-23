class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.ans_len = len(nums)
        chain = [None] * self.ans_len
        self.index = 0
        current_num = nums[self.index]
        self.breakdown(current_num, chain, self.index)
        return self.ans
        
    def breakdown(self, current_num, chain, index):
        # If we have a full answer, add to list and return.
        if index == self.ans_len:
            self.ans.append(chain)
            return
        # Make a local copy of chain to manipulate.
        local_chain = chain.copy()
        # Loop through all the numbers in nums and insert into chain at index point, then move to next index.
        for num in self.nums:
            if num in local_chain:
                continue
            local_chain[index] = num
            self.breakdown(num, local_chain, index+1)
