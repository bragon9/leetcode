import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x, y = len(grid[0]), len(grid)
        # Initialize the min_score_grid.  The important thing is that there is only 1 path when y=0 (straight right).
        subtotal = 0
        min_score_grid = []
        first_row = []
        # Set the first row to be the cumulative sum as you move right.
        for value in grid[0]:
            subtotal += value
            first_row.append(subtotal)
        min_score_grid.append(first_row)
        # Initialize the rest of the values to infinity so we can compare.
        for i in range(y-1):
            min_score_grid.append([math.inf] * x)
        # Loop through all the possible squares and the possible paths to the current square is the paths to the squares directly above (y-1) and left (x-1).
        for y_ptr in range(1, y):
            for x_ptr in range(x):
                curr_score = grid[y_ptr][x_ptr]
                # If we are on the leftmost row, you can only get here from the above square.
                if x_ptr == 0:
                    min_score_grid[y_ptr][x_ptr] = min_score_grid[y_ptr-1][x_ptr] + curr_score
                else:
                    # Take the minimum score of the left or above square.
                    min_score_grid[y_ptr][x_ptr] = min(min_score_grid[y_ptr-1][x_ptr], min_score_grid[y_ptr][x_ptr-1]) + curr_score        
        return min_score_grid[y-1][x-1]
