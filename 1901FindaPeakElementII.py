class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        def get_neighbors(x, y):
            neighbors = []
            offsets = [(-1,0),(1,0),(0,-1),(0,1)]
            for x_offset, y_offset in offsets:
                new_x = x + x_offset
                new_y = y + y_offset
                if (0 <= new_y <= len(mat)-1) and (0 <= new_x <= len(mat[0])-1):
                        neighbors.append((new_x, new_y))
            return neighbors
        
        def get_max(arr):
            hi = 0
            for arr_x, arr_y in arr:
                if mat[arr_y][arr_x] > hi:
                    hi = mat[arr_y][arr_x]
                    coords = [arr_x, arr_y]
            return hi, coords
                    
        ans = []
        # Start in the middle of the matrix.
        x = (len(mat[0])-1)//2
        y = (len(mat)-1)//2
        while True:
            curr = mat[y][x]
            neighbors = get_neighbors(x, y)
            hi, hi_coords = get_max(neighbors)
            if curr > hi:
                return [y, x]
            else:
                x, y = hi_coords
            
            
