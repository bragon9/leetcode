class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k > n:
            return -1
        if k == 1:
            return 1
        ans = 2
        ptr = 2
        while ans <= n:
            while n % ans != 0:
                ans += 1
            if ptr > k:
                return -1
            if ptr == k:
                return ans
            ans += 1
            ptr += 1
        return -1
