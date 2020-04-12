class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            high, low = 0, 0
            for i in range(len(stones)):
                if stones[i] > high:
                    high = stones[i]
                    hi_ptr = i
            for i in range(len(stones)):
                if i == hi_ptr:
                    continue
                if stones[i] > low:
                    low = stones[i]
                    lo_ptr = i
            difference = abs(stones[lo_ptr] - stones[hi_ptr])
            max_ptr = max(lo_ptr, hi_ptr)
            min_ptr = min(lo_ptr, hi_ptr)
            if difference:
                stones[max_ptr] = difference
            else:
                stones.pop(max_ptr)
            stones.pop(min_ptr)
        return sum(stones)
