class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        # From topright corner, walk left and see how many columns of full negative numbers there are.
        cols = 0
        for i in range(len(grid[0])-1, -1, -1):
            if grid[0][i] >= 0:
                break
            cols += 1
        ans += len(grid) * cols
        x_end = len(grid[0])-cols-1
        # From bottom left corner, walk up and see how many rows of full negative numbers there are.
        rows = 0
        for i in range(len(grid)-1, -1, -1):
            if grid[i][0] >= 0:
                break
            rows += 1
        ans += len(grid[0][:x_end+1]) * rows
        y_end = len(grid)-rows-1
        # Loop through the rest from the topleftmost insersection point of a full row and full column.
        for y in range(y_end, -1, -1):
            for x in range(x_end, -1, -1):
                if grid[y][x] < 0:
                    ans += 1
                else:
                    break
        return ans
                
        
