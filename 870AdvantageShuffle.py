from collections import defaultdict

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sorted_a = sorted(A)
        sorted_b = sorted(B)
        ans_dict = defaultdict(list)
        leftovers = []
        ans = []
        ptr_a = ptr_b = 0
        while ptr_a < len(A):
            val_a = sorted_a[ptr_a]
            val_b = sorted_b[ptr_b]
            if val_a > val_b:
                ans_dict[val_b].append(val_a)
                ptr_a += 1
                ptr_b += 1
            else:
                leftovers.append(val_a)
                ptr_a += 1
        for val in B:
            if val in ans_dict and ans_dict[val]:
                ans.append(ans_dict[val].pop())
            else:
                ans.append(leftovers.pop())
        return ans
