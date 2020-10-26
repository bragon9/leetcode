class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        if query_glass == query_row == 0:
            return 1
        glass = Glass(poured, 0, 0)
        row = [glass]
        while True:
            next_row = []
            ptr = 0
            overflow = False
            for glass in row:
                if glass.row == query_row and glass.glass == query_glass:
                    return glass.amount
                # Create first glass.
                if ptr == 0:
                    if glass.overflow:
                        left = Glass(glass.overflow/2, glass.row+1, ptr)
                        overflow = True
                    else:
                        left = Glass(0, glass.row+1, ptr)
                    next_row.append(left)
                    ptr += 1
                # Glass already exists.
                else:
                    if glass.overflow:
                        next_row[-1].pour(glass.overflow/2)
                        overflow = True
                right = Glass(glass.overflow/2, glass.row+1, ptr)
                next_row.append(right)
                ptr += 1
            row = next_row
            if not(overflow):
                return 0

class Glass:
    def __init__(self, amount, row, glass):
        if amount >= 1:
            self.overflow = amount - 1
            self.amount = 1
        else:
            self.amount = amount
            self.overflow = 0
        self.row = row
        self.glass = glass
        
    def pour(self, amount):
        if self.amount == 1:
            self.overflow += amount
        else:
            self.amount += amount
            if self.amount > 1:
                self.overflow += self.amount - 1
                self.amount =1
            
    def __str__(self):
        print(f'Glass at {self.row=}, {self.glass=}, {self.amount=}, {self.overflow=}')
