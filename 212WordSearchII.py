class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        # key = letter, value = set of coords
        self.letter_dict = {}
        self.max_y = len(board)
        self.max_x = len(board[0])
        for y in range(self.max_y):
            for x in range(self.max_x):
                letter = board[y][x]
                coords = (x, y)
                if letter in self.letter_dict:
                    self.letter_dict[letter].add(coords)
                else:
                    self.letter_dict[letter] = set([coords])
        ans = []
        for word in words:
            if self.search(word, 0, None, set()):
                ans.append(word)
        return ans
    
    def search(self, word, ptr, pos, visited):
        if ptr == len(word):
            return True
        letter = word[ptr]
        if letter not in self.letter_dict:
            return False
        if ptr == 0:
            for coord in self.letter_dict[letter]:
                visited_copy = visited.copy()
                visited_copy.add((coord))
                if self.search(word, ptr+1, coord, visited_copy):
                    return True
        else:
            neighbors = self.get_neighbors(pos)
            letter_coords = self.letter_dict[letter]
            for coord in letter_coords:
                if coord in neighbors and coord not in visited:
                    visited_copy = visited.copy()
                    visited_copy.add((coord))
                    if self.search(word, ptr+1, coord, visited_copy):
                        return True
        return False
        
    def get_neighbors(self, pos):
        neighbors = set()
        x, y = pos
        if x > 0:
            neighbors.add((x-1, y))
        if x < self.max_x:
            neighbors.add((x+1, y))
        if y > 0:
            neighbors.add((x, y-1))
        if y < self.max_y:
            neighbors.add((x, y+1))
        return neighbors
            
        
        
