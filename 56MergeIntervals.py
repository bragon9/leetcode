class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = []
        sub_ans = []
        lo, hi = intervals[0]
        for i in range(1, len(intervals)):
            int_lo, int_hi = intervals[i]
            # This interval fits into previous one
            if lo <= int_lo <= int_hi <= hi:
                continue
            # This interval overlaps with previous
            if int_lo <= hi <= int_hi:
                hi = int_hi
            else:
                # This interval does not overlap.
                ans.append([lo, hi])
                lo = int_lo
                hi = int_hi
        ans.append([lo,hi])
        return ans
            
