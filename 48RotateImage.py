class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Flip upside down.
        halfway = len(matrix)//2 + len(matrix) % 2
        for y in range(halfway):
            for x in range(len(matrix)):
                matrix[y][x], matrix[len(matrix) - y - 1][x] = matrix[len(matrix) - y - 1][x], matrix[y][x]
        # Flip symmetry. Loop this way so you don't flip values that already flipped.
        for y in range(len(matrix)):
            for x in range(y, len(matrix)):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
