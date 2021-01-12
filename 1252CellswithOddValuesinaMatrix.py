from collections import defaultdict

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # Initialize matrix to all 0's.
        init_row = [0] * m
        matrix = []
        for _ in range(n):
            matrix.append(init_row.copy())
        # Loop through indices to see how much to add to each row/col.
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        for ri, ci in indices:
            row_dict[ri] += 1
            col_dict[ci] += 1
        ans = 0
        # Loop through matrix and increment each cell by amount from dictionaries.
        for row in range(n):
            for col in range(m):
                matrix[row][col] += row_dict[row] + col_dict[col]
                if matrix[row][col] % 2:
                    ans += 1
        return ans
