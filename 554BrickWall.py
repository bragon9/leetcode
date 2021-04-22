class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        holes_dict = {}
        ans = 0
        # Find the column with the most "holes"
        for row in wall:
            prev = 0
            for i in range(len(row)-1):
                hole = row[i] + prev
                if hole in holes_dict:
                    holes_dict[hole] += 1
                else:
                    holes_dict[hole] = 1
                if holes_dict[hole] > ans:
                    ans = holes_dict[hole]
                prev += row[i]
        # Return number of bricks - number of holes = bricks you have to go through
        return len(wall) - ans
