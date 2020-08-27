from bisect import insort

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_starts = []
        sorted_ends = []
        for index, interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            start_val = [start, index]
            end_val = [end, index]
            insort(sorted_starts, start_val)
            insort(sorted_ends, end_val)
        
        ans = [-1] * len(intervals)
        search = 0
        # Loop through all the ends and find the nearest start.
        for end, index in sorted_ends:
            # If we've checked all the starts, the rest will not have an answer.
            if search >= len(sorted_starts):
                return ans
            for i in range(search, len(sorted_starts)):
                start = sorted_starts[i][0]
                if start >= end:
                    search = i
                    ans[index] = sorted_starts[i][1]
                    break
        return ans
