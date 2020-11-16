class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ans = 0
        count = 0
        trend = None
        for i in range(1, len(A)):
            prev = A[i-1]
            curr = A[i]
            # Up
            if curr > prev:
                if trend == 'UP':
                    count += 1
                else: 
                    ans = max(ans, count)
                    count = 2
                    trend = 'UP'
            # Down
            elif curr < prev:
                if trend == 'UP':
                    count += 1
                    trend = 'DOWN'
                elif trend == 'DOWN':
                    count += 1
                else:
                    continue
            # Flat
            else:
                if trend == 'DOWN':
                    ans = max(ans, count)
                trend = None
                count = 0
        if count and trend == 'DOWN':
            return max(ans, count)
        else:
            return ans
                    
