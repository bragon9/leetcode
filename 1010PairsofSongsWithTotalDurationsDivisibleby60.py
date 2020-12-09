class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0]*60
        ans = 0
        for duration in time:
            duration = duration%60
            ans += arr[(60-duration)%60]
            arr[duration] += 1
        return ans
