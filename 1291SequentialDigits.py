class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.ans = []
        self.low = low
        self.high = high
        str_low = str(low)
        str_high = str(high)
        for i in range(len(str_low), len(str_high)+1):
            self.recurse(i, 0)
        return self.ans
            
    def recurse(self, target, length, ans=0):
        if ans > self.high:
            return
        if length == target:
            if ans >= self.low:
                self.ans.append(ans)
            return
        elif length > target:
            return
        prev_char = str(ans)[-1]
        ans *= 10
        for i in range(1,10):
            if i - int(prev_char) == 1 or prev_char == '0':
                self.recurse(target, length+1, ans + i)
            elif i - int(prev_char) >= 2:
                break
