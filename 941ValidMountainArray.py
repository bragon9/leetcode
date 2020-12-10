class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Not valid
        if len(arr) < 3:
            return False
        ptr = 1
        up = False
        # Climb up as long as possible
        while arr[ptr] > arr[ptr-1]:
            up = True
            ptr += 1
            if ptr >= len(arr):
                return False
        # Climb down as long as possible
        while arr[ptr] < arr[ptr-1]:
            ptr += 1
            # If we hit the end of the array AND have climbed up, it is valid
            if ptr >= len(arr):
                return up
        return False


            
