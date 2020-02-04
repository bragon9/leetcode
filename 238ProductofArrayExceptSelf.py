class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        always_zero = False
        right_prod_arr = nums.copy()
        # Loop through in reverse to store the consecutive product in the right_prod_arr.
        for i in range(len(nums)-2, -1, -1):
            right_prod_arr[i] *= right_prod_arr[i+1]
        for index in range(len(nums)):
            # If it's the first item, left product is 1 to just return right product.
            if index == 0:
                left_prod = 1
            # Else, just add the newest number to the previous left product.
            else:
                newest_left = nums[index-1]
                left_prod *= newest_left
            # If it's the last item, right_prod is 1 to just return left product.
            if index == len(nums)-1:
                right_prod = 1
            # Else, use the stored product.
            else:
                right_prod = right_prod_arr[index+1]
            ans.append(left_prod * right_prod)
        return ans
