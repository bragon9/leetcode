class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        self.target = target
        self.candidates = candidates
        self.get_combos()
        return self.ans
        
    def get_combos(self, current_ans=[], current_sum=0):
        if current_sum == self.target:
            sorted_ans = tuple(sorted(current_ans))
            if sorted_ans not in self.ans:
                self.ans.add(sorted_ans)
            return
        elif current_sum > self.target:
            return
        for num in self.candidates:
            self.get_combos(current_ans + [num], current_sum + num)
