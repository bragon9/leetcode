class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        curr_x, curr_y = points[0][0], points[0][1]
        seconds = 0
        # Find the amount we can move diagonally, then the rest is a straight line.
        for point in points[1:]:
            next_x, next_y = point[0], point[1]
            x_distance, y_distance = abs(next_x - curr_x), abs(next_y - curr_y)
            max_distance, min_distance = max(x_distance, y_distance), min(x_distance, y_distance)
            seconds += min_distance + (max_distance - min_distance)
            curr_x, curr_y = next_x, next_y
        return seconds
                    
            
