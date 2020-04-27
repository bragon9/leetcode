class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not(matrix):
            return 0
        ans = 0
        self.max_y = len(matrix)
        self.max_x = len(matrix[0])
        # Loop through and for every '1', determine the area of the square it is the topleft corner of.
        for y in range(self.max_y):
            for x in range(self.max_x):
                value = matrix[y][x]
                if value == '1':
                    area = self.get_area(matrix, x, y) ** 2
                    ans = max(ans, area)
        return ans
    
    def get_area(self, matrix, x, y):
        # Increases x and y by 1 incrementally, then checks to see if the new row/column is all "1"s.
        offset = 1
        # Loop until we reach either edge of the matrix
        while (x + offset < self.max_x) and (y+offset < self.max_y):
            for i in range(0, offset+1):
                # Loop until we reach either edge of the matrix
                if (y+i > self.max_y) or (x+i > self.max_x):
                    return offset
                # Check column
                if matrix[y+i][x+offset] == '0':
                    return offset
                # Check row
                if matrix[y+offset][x+i] == '0':
                    return offset
            offset += 1
        return offset

                

        
        
