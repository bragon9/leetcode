from bisect import bisect_left

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        search = mat[0][0]
        while True:
            found = True
            for arr in mat:
                index = bisect_left(arr, search)
                if index >= len(arr):
                    return -1
                if arr[index] == search:
                    continue
                else:
                    found = False
                    search = arr[index]
            if found:
                return search
            
