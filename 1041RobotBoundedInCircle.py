class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        directions = ['N','E','S','W']
        ptr = 0
        for _ in range(1):
            for code in instructions:
                if code == 'L' or code == 'R':
                    ptr = self.turn(ptr, code)
                else:
                    x,y = self.move(x, y, directions[ptr])
        return (x, y) == (0, 0) or ptr != 0
        
    def turn(self, ptr, code):
        if code == 'L':
            if ptr > 0:
                return ptr-1
            else:
                return 3
        elif code == 'R':
            if ptr < 3:
                return ptr+1
            else:
                return 0
            
    def move(self, x, y, direction):
        if direction == 'N':
            return (x, y+1)
        elif direction == 'E':
            return (x+1,y)
        elif direction == 'S':
            return (x,y-1)
        elif direction == 'W':
            return (x-1,y)
        
            
