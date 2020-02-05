class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            sub_ans = []
            for combo in ans:
                sub_ans.append(combo + [num])
            ans.extend(sub_ans)
        return ans
