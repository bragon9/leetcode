class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x, y = m, n
        # Initialize the possible paths array.  The important thing is that there is only 1 path when y=0 (straight right).
        paths = [[1 for _ in range(x)] for _ in range(y)]
        # Loop through all the possible squares and the possible paths to the current square is the paths to the squares directly above (y-1) and left (x-1).
        for y_ptr in range(1, y):
            for x_ptr in range(1, x):
                paths[y_ptr][x_ptr] = paths[y_ptr-1][x_ptr] + paths[y_ptr][x_ptr-1]
        # Return with -1 due to zero indexing in the arrays vs startingn at (1,1).
        return paths[y-1][x-1]
