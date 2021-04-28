class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = [0] * len(obstacleGrid[0]) 
        dp = []
        # Create an array the size of obstacleGrid to use for DP
        for _ in range(len(obstacleGrid)):
            dp.append(row.copy())
        # One path along the top row to the right.  If obstacle in the way, stop.
        for i in range(len(dp[0])):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        # One path along the first column downward.  If obstacle in the way, stop.
        for i in range(len(dp)):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        # Walk through from 2nd column of every row starting on 2nd row.
        # Possible paths are number possible above + number possible to the left.
        # If the spot is a rock, number of possibilities are 0.
        for y in range(1, len(obstacleGrid)):
            for x in range(1, len(obstacleGrid[y])):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
        # Return answer for the bottom-right-most coordinate.
        return dp[-1][-1]
            
