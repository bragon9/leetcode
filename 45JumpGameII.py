class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0
        max_range = 0
        jumps = 0
        # Loop through until we can reach the end.
        while max_range < len(nums)-1:
            furthest = 0
            # Loop through every index from current position up to the max_range index
            for i in range(curr, max_range+1):
                # Check how far each index can jump to.
                furthest = max(furthest, i + nums[i])
            # Set new curr to max_range+1, and max_range to the furthest possible.
            curr, max_range = max_range+1, furthest
            jumps += 1
        return jumps
            
