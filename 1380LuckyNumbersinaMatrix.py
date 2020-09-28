from math import inf

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        self.max_col_dict = {}
        ans = []
        for row in matrix:
            min_num = inf
            min_index = 0
            for index, value in enumerate(row):
                if value < min_num:
                    min_num = value
                    min_index = index
            # Check if the minimum in the row is the max in the column.
            if min_num == self.get_max_col(matrix, min_index):
                ans.append(min_num)
        return ans
                
    def get_max_col(self, matrix, index):
        # Get the max number in the column.
        if index in self.max_col_dict:
            return self.max_col_dict[index]
        max_num = -inf
        for row in (matrix):
            num = row[index]
            if num > max_num:
                max_num = num
        self.max_col_dict[index] = max_num
        return max_num
            
