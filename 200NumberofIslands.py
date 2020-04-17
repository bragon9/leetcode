from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not(grid):
            return 0
        self.visited = set()
        self.max_x = len(grid[0])
        self.max_y = len(grid)
        num_islands = 0
        for y in range(self.max_y):
            for x in range(self.max_x):
                if (x, y) not in self.visited:
                    if grid[y][x] == '1':
                        self.visit_island(x, y, grid)
                        num_islands += 1
        return num_islands
                        
    def visit_island(self, x, y, grid):
        to_visit = deque()
        to_visit.append((x, y))
        while to_visit:
            (x, y) = to_visit.pop()
            if (x, y) not in self.visited:
                self.visited.add((x, y))
                if grid[y][x] == '1':
                    up_y = y-1
                    if up_y >= 0:
                        to_visit.append((x, up_y))
                    down_y = y+1
                    if down_y < self.max_y:
                        to_visit.append((x, down_y))
                    left_x = x-1
                    if left_x >= 0:
                        to_visit.append((left_x, y))
                    right_x = x+1
                    if right_x < self.max_x:
                        to_visit.append((right_x, y))
