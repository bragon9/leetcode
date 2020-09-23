class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        # Length of solution
        self.count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    start = (x,y)
                if grid[y][x] == 2:
                    end = (x,y)
                if grid[y][x] != -1:
                    self.count += 1
        self.max_x = x
        self.max_y = y
        self.end = end
        self.ans = 0
        self.walk(start, set())
        return self.ans
    
    def walk(self, pos, visited):
        x, y = pos
        # Check for solution (at end and stepped on every square once)
        if pos == self.end and len(visited) == self.count-1:
            self.ans += 1
            return
        visited.add(pos)
        to_visit = []
        if x > 0:
            to_visit.append((x-1,y))
        if x < self.max_x:
            to_visit.append((x+1,y))
        if y > 0:
            to_visit.append((x,y-1))
        if y < self.max_y:
            to_visit.append((x,y+1))
        for coords in to_visit:
            if coords not in visited:
                check_x, check_y = coords
                if self.grid[check_y][check_x] != -1:
                    self.walk(coords, visited.copy())
        
