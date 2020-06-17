class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not(board):
            return
        self.max_y = len(board)-1
        self.max_x = len(board[0])-1
        visited = set()
        for y in range(len(board)):
            for x in range(len(board[0])):
                value = board[y][x]
                if (x, y) not in visited and value == 'O':
                    self.capture(x, y, board, visited)
                    
    def capture(self, x, y, board, visited):
        """
        Given x, y will find the total area of O's.
        If none are touching an edge, it will capture the area.
        """
        to_visit = [(x, y)]
        area = set()
        valid = True
        # DFS the board.
        while to_visit:
            curr_pos = to_visit.pop()
            x, y = curr_pos
            if (x, y) in visited:
                continue
            visited.add((x, y))
            area.add((x, y))
            # The current space on the board is on an edge, making the area invalid for capture.
            if x == 0 or x == self.max_x or y == 0 or y == self.max_y:
                valid = False
            # Add all neighbors that are 'O' to to_visit.
            neighbors = self.get_neighbors(x, y)
            for x1, y1 in neighbors:
                if board[y1][x1] == 'O':
                    to_visit.append((x1, y1))
        # If the whole area is valid, capture it.
        if valid:
            for x_cap, y_cap in area:
                board[y_cap][x_cap] = 'X'
                
    def get_neighbors(self, x, y):
        # Gets all neighbors within the board. 
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if x < self.max_x:
            neighbors.append((x+1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if y < self.max_y:
            neighbors.append((x, y+1))
        return neighbors
            
