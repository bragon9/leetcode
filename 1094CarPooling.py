class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stop_list = [0] * 1001
        max_stop = 0
        for passengers, start, stop in trips:
            stop_list[start] += passengers
            stop_list[stop] -= passengers
            max_stop = max(max_stop, stop)
        current_riders = 0
        for i in range(max_stop+1):
            current_riders += stop_list[i]
            if current_riders > capacity:
                return False
        return True
        
