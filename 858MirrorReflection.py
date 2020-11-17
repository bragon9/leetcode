class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        R = 'RIGHT'
        L = 'LEFT'
        U = 'UP'
        D = 'DOWN'
        
        y = 0
        y_dir = U
        x_dir = L
        while True:
            # Switch X
            if x_dir == R:
                x_dir = L
            else:
                x_dir = R
            # Move y
            if y_dir == U:
                y += q
            if y_dir == D:
                y -= q
            # See if it went out of bounds for Y
            if y > p:
                diff = y-p
                y = p-diff
                y_dir = D
            if y < 0:
                y = -y
                y_dir = U
            # print(f'{y=}, {x_dir=}, {y_dir=}')
            # Check for corner
            if y == p:
                if x_dir == L:
                    return 2
                else:
                    return 1
            if y == 0 and x_dir == R:
                return 0
