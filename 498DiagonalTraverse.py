class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not(matrix):
            return matrix
        direction = 'L'
        x = y = 0
        self.ans = []
        self.max_x = len(matrix[0])
        self.max_y = len(matrix)
        for i in range(self.max_x+self.max_y-1):
            if direction == 'R':
                direction = 'L'
            else:
                direction = 'R'
            (x, y) = self.traverse(matrix, x, y, direction)
        return self.ans
    
    def traverse(self, matrix, x, y, direction):
        self.ans.append(matrix[y][x])
        if direction == 'R':
            # Walk right and up
            while x < self.max_x-1 and y > 0:
                x += 1
                y -= 1
                self.ans.append(matrix[y][x])
            # Move to start of next row
            if x < self.max_x-1:
                x += 1
            else:
                y += 1
        else:
            # Walk down and left
            while x > 0 and y < self.max_y-1:
                x -= 1
                y += 1
                self.ans.append(matrix[y][x])
            # Move to start of next row
            if y < self.max_y-1:
                y += 1
            else:
                x += 1
        return (x, y)
                
            
