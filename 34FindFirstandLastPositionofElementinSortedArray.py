class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bi_search():
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (hi+lo)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid-1
                elif nums[mid] < target:
                    lo = mid+1
            # Check if it was in array
            if lo < len(nums) and nums[lo] == target:
                return lo
            else:
                return -1
            
        if not(nums):
            return [-1, -1]
        i = bi_search()
        if i == -1:
            return [i, i]
        b = f = i
        # Loop through backwards and forwards to get all indices contain target number
        while b >= 0 and nums[b] == target:
            b -= 1
        while f < len(nums) and nums[f] == target:
            f += 1
        return [b+1, f-1]
                
