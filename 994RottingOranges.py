class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.max_y = len(grid)-1
        self.max_x = len(grid[0])-1
        self.visited = set()
        self.ans = 0
        rot = True
        while rot:
            coord_list = []
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 2 and (x,y) not in self.visited:
                        coord_list.append((x,y))
            rot = self.rot(coord_list)
            if rot:
                self.ans += 1
            else:
                for y in range(len(grid)):
                    for x in range(len(grid[0])):
                        if grid[y][x] == 1:
                            return -1
                if self.ans:
                    return self.ans
                else:
                    return 0
        return self.ans
    
    def rot(self, coord_list):
        change = False
        for coord in coord_list:
            (x,y) = coord
            to_rot = []
            if x > 0 and self.grid[y][x-1] == 1:
                change = True
                self.grid[y][x-1] = 2
            if x < self.max_x and self.grid[y][x+1] == 1:
                change = True
                self.grid[y][x+1] = 2
            if y > 0 and self.grid[y-1][x] == 1:
                change = True
                self.grid[y-1][x] = 2
            if y < self.max_y and self.grid[y+1][x] == 1:
                change = True
                self.grid[y+1][x] = 2
            self.visited.add(coord)
        return change
