class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cum_sums = []
        for row in matrix:
            row_arr = []
            cum_sum = 0
            for num in row:
                cum_sum += num
                row_arr.append(cum_sum)
            self.cum_sums.append(row_arr)
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == row2 == col1 == col2:
            return self.matrix[row1][col1]
        ans = 0
        for i in range(row1, row2+1):
            if col1 >= 1:
                ans += self.cum_sums[i][col2] - self.cum_sums[i][col1-1]
            else:
                ans += self.cum_sums[i][col2]
        return ans
