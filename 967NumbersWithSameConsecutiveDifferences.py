class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.ans = set()
        if N == 1:
            for i in range(10):
                self.recurse(i, N, K, 1, i)
        else:
            for i in range(1, 10):
                self.recurse(i, N, K, 1, i)
        return self.ans

    def recurse(self, sub_ans, N, K, length, last):
        if length == N:
            self.ans.add(sub_ans)
            return
        if last - K >= 0:
            self.recurse(sub_ans*10 + last-K, N, K, length+1, last-K)
        if last + K < 10:
            self.recurse(sub_ans*10 + last+K, N, K, length+1, last+K)
