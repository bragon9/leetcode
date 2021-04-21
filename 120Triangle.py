class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle.copy()
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    ans[i][j] = triangle[i][j] + ans[i-1][j]
                elif j == len(triangle[i])-1:
                    ans[i][j] = triangle[i][j] + ans[i-1][j-1]
                else:
                    ans[i][j] = triangle[i][j] + min(ans[i-1][j-1], ans[i-1][j])
        return min(ans[-1])
