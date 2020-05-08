class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Compare first two points as a baseline.
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        # Find slope:
        if x1 == x2:
            # horizontal line.
            for coord in coordinates[2:]:
                if coord[0] != x1:
                    return False
        elif y1 == y2:
            # vertical line
            for coord in coordinates[2:]:
                if coord[1] != y1:
                    return False
        else:
            # Sloped line
            slope = (y2 - y1) / (x2 - x1)
            for coords in coordinates[2:]:
                x, y = coords[0], coords[1]
                curr_slope = ((y - y1) / (x - x1))
                if curr_slope != slope:
                    return False
        return True
