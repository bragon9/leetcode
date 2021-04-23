class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        arr = []
        count = 1
        prev = s[0]
        for letter in s[1:]:
            if letter == prev:
                count += 1
            else:
                arr.append(count)
                count = 1
            prev = letter
        arr.append(count)
        ans = 0
        for i in range(1, len(arr)):
            ans += min(arr[i], arr[i-1])
        return ans
            
