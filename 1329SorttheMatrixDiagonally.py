class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort_diag(x, y):
            ''' Given an x and y, sort the diagonal moving down and right'''
            arr = []
            while x < len(mat[0]) and y < len(mat):
                bisect.insort(arr, mat[y][x])
                x += 1
                y += 1
            return arr

        # Loop through top row except last cell
        for x in range(len(mat[0])-1):
            sorted_arr = sort_diag(x, 0)
            x_ptr = x
            y_ptr = 0
            # Set the diagonal moving down/right with the sorted values
            for num in sorted_arr:
                mat[y_ptr][x_ptr] = num
                x_ptr += 1
                y_ptr += 1
        # Loop through the first cell of all rows except 1st and last
        for y in range(1, len(mat)-1):
            sorted_arr = sort_diag(0, y)
            x_ptr = 0
            y_ptr = y
            # Set the diagonal moving down/right with the sorted values
            for num in sorted_arr:
                mat[y_ptr][x_ptr] = num
                x_ptr += 1
                y_ptr += 1
        return mat
