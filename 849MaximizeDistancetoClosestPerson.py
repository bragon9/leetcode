class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        EMPTY = 0
        TAKEN = 1
        # First item is streak of empty chairs, second item is boolean if it's sandwiched (True) or open on one end (False)
        chain = [0, False]
        ans = 0
        for seat in seats:
            if seat == EMPTY:
                chain[0] += 1
            if seat == TAKEN:
                if chain[0]:
                    ans = max(ans, self.calc(chain))
                # After the first taken seat, rest are sandwiched, unless the last seat is open
                chain = [0, True]
        # Last seat was open if we ended with a chain value. Set to open ended and calculate.
        if chain[0]:
            chain[1] = False
            ans = max(self.calc(chain), ans)
        return ans
    
    def calc(self, chain):
        # Return distance to person depending if it's sandwiched or not
        num_chairs, sandwich = chain
        if sandwich:
            return (num_chairs // 2) + (num_chairs % 2)
        else:
            return num_chairs
