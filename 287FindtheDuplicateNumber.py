class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)-1
        # Loop through whole array counting numbers that are <= mid.
        while low < high:
            mid = (high + low) // 2 
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # If there are more numbers than there should be <= mid, search again in the lower half.
            if count > mid:
                high = mid
            # If there are the correct amount, the duplicate is in the higher half.
            else:
                low = mid + 1
        # Once low and high converge, we have the correct value.
        return low
        
