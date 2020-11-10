class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not(A):
            return A
        for row in A:
            # If there is only 1 char, invert it
            if len(row) == 1:
                if row[0] == 1:
                    row[0] = 0
                else:
                    row[0] = 1
            else:
                # Loop through til midpoint, swapping and inverting
                for i in range(len(row)//2):
                    f = row[i]
                    hold = row[-(i+1)]
                    if f == 0:
                        row[-(i+1)] = 1
                    else:
                        row[-(i+1)] = 0
                    if hold == 0:
                        row[i] = 1
                    else:
                        row[i] = 0
                # If midpoint exists (odd row len), invert middle.
                if len(row) % 2:
                    m = (len(row)//2)
                    if row[m] == 0:
                        row[m] = 1
                    else:
                        row[m] = 0
        return A    
                    
        
