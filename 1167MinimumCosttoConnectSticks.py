from heapq import heapify, heappush, heappop

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        stick_heap = sticks
        heapify(stick_heap)
        ans = 0
        while len(stick_heap) > 1:
            a = heappop(stick_heap)
            b = heappop(stick_heap)
            ans += a + b
            heappush(stick_heap, a+b)
        return ans
        
