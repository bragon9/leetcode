class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            ans.append([0] * n)
        ptr = 1
        x = -1
        y = 0
        offset = 0
        while ptr <= n**2:
            for i in range(n-offset):
                x += 1
                if ans[y][x] == 0:
                    ans[y][x] = ptr
                ptr += 1
            for i in range(n-offset-1):
                y += 1
                if ans[y][x] == 0:
                    ans[y][x] = ptr
                ptr += 1
            for i in range(n-offset-1):
                x -= 1
                if ans[y][x] == 0:
                    ans[y][x] = ptr
                ptr += 1
            for i in range(n-offset-2):
                y -= 1
                if ans[y][x] == 0:
                    ans[y][x] = ptr
                ptr += 1
            offset += 2
        return ans
            
