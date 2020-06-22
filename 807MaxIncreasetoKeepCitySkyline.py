class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        front = [0] * len(grid)
        side = [0] * len(grid[0])    
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                curr_value = grid[y][x]
                if curr_value > side[y]:
                    side[y] = curr_value
                if curr_value > front[x]:
                    front[x] = curr_value
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                curr_val = grid[y][x]
                max_val = min(front[x], side[y])
                ans += max_val - curr_val
        return ans
